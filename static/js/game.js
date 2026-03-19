/* The Gambit front-end scene manager.
 *
 * Handles:
 * - API calls to Flask backend
 * - Scene rendering and transitions
 * - Typewriter effect
 * - Save/load modal
 * - Ending summary overlay
 * - Lightweight autosave marker in localStorage
 */

const API = {
  state: "/api/state",
  start: "/api/start",
  choice: "/api/choice",
  restart: "/api/restart",
  save: "/api/save",
  saves: "/api/saves",
  load: "/api/load",
};

const STORAGE_KEY = "the_gambit_has_active_run";

const els = {
  titleScreen: document.getElementById("title-screen"),
  gameScreen: document.getElementById("game-screen"),
  titleStatus: document.getElementById("title-status"),

  btnStart: document.getElementById("btn-start"),
  btnContinue: document.getElementById("btn-continue"),
  btnLoadMenu: document.getElementById("btn-load-menu"),

  hudChapter: document.getElementById("hud-chapter"),
  hudSceneTitle: document.getElementById("hud-scene-title"),
  progressBar: document.getElementById("progress-bar"),
  progressLabel: document.getElementById("progress-label"),

  sceneTags: document.getElementById("scene-tags"),
  sceneText: document.getElementById("scene-text"),
  choicesList: document.getElementById("choices-list"),

  inventoryList: document.getElementById("inventory-list"),
  statsList: document.getElementById("stats-list"),
  pathList: document.getElementById("path-list"),

  btnSave: document.getElementById("btn-save"),
  btnLoad: document.getElementById("btn-load"),
  btnRestart: document.getElementById("btn-restart"),

  saveModal: document.getElementById("save-modal"),
  saveSlotList: document.getElementById("save-slot-list"),
  btnCloseModal: document.getElementById("btn-close-modal"),

  endingModal: document.getElementById("ending-modal"),
  endingTitle: document.getElementById("ending-title"),
  endingSummary: document.getElementById("ending-summary"),
  endingPath: document.getElementById("ending-path"),
  btnEndingRestart: document.getElementById("btn-ending-restart"),
  btnEndingClose: document.getElementById("btn-ending-close"),
};

const uiState = {
  latestState: null,
  latestScene: null,
  typingInProgress: false,
};

async function apiRequest(url, options = {}) {
  const response = await fetch(url, {
    method: options.method || "GET",
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    body: options.body ? JSON.stringify(options.body) : undefined,
  });

  const data = await response.json();
  if (!response.ok || !data.ok) {
    const message = data && data.error ? data.error : "Unexpected error.";
    throw new Error(message);
  }
  return data;
}

function showTitleScreen(statusText = "No active run loaded.") {
  els.titleScreen.classList.remove("hidden");
  els.gameScreen.classList.add("hidden");
  els.titleStatus.textContent = statusText;
}

function showGameScreen() {
  els.titleScreen.classList.add("hidden");
  els.gameScreen.classList.remove("hidden");
}

function setButtonsDisabled(disabled) {
  [els.btnSave, els.btnLoad, els.btnRestart, els.btnStart, els.btnContinue].forEach((btn) => {
    if (btn) {
      btn.disabled = disabled;
    }
  });
}

function animateSceneSwap() {
  els.sceneText.classList.remove("fade-in");
  void els.sceneText.offsetWidth;
  els.sceneText.classList.add("fade-in");
}

function createTagPill(tag) {
  const span = document.createElement("span");
  span.className = "tag-pill";
  span.textContent = tag;
  return span;
}

async function typewriterParagraph(container, text, speed = 11) {
  return new Promise((resolve) => {
    const p = document.createElement("p");
    p.className = "story-paragraph typewriter-caret";
    container.appendChild(p);

    let idx = 0;
    const timer = setInterval(() => {
      idx += 1;
      p.textContent = text.slice(0, idx);
      if (idx >= text.length) {
        clearInterval(timer);
        p.classList.remove("typewriter-caret");
        resolve();
      }
    }, speed);
  });
}

async function renderSceneText(paragraphs) {
  uiState.typingInProgress = true;
  els.sceneText.innerHTML = "";

  for (const paragraph of paragraphs) {
    // Short dramatic pause between paragraphs to improve pacing.
    // eslint-disable-next-line no-await-in-loop
    await typewriterParagraph(els.sceneText, paragraph);
    // eslint-disable-next-line no-await-in-loop
    await new Promise((resolve) => setTimeout(resolve, 120));
  }

  uiState.typingInProgress = false;
}

function renderChoices(choices) {
  els.choicesList.innerHTML = "";

  if (!choices || choices.length === 0) {
    const fallback = document.createElement("p");
    fallback.textContent = "No choices available in this scene.";
    fallback.className = "modal-sub";
    els.choicesList.appendChild(fallback);
    return;
  }

  for (const choice of choices) {
    const button = document.createElement("button");
    button.className = "choice-btn";
    button.dataset.choiceId = choice.id;
    button.innerHTML = `<strong>${choice.label}</strong>`;

    if (choice.note) {
      const note = document.createElement("span");
      note.className = "choice-note";
      note.textContent = choice.note;
      button.appendChild(note);
    }

    button.addEventListener("click", async () => {
      await onChoice(choice.id);
    });

    els.choicesList.appendChild(button);
  }
}

function renderInventory(inventory) {
  els.inventoryList.innerHTML = "";
  const printable = Object.entries(inventory || {});

  for (const [key, value] of printable) {
    const li = document.createElement("li");
    const label = key.replaceAll("_", " ");
    li.textContent = `${label}: ${value}`;
    els.inventoryList.appendChild(li);
  }
}

function renderStats(state, scene) {
  els.statsList.innerHTML = "";
  const metrics = [
    ["Choices made", state?.stats?.choices_made ?? 0],
    ["Endings unlocked", state?.stats?.endings_unlocked ?? 0],
    ["Chapters seen", state?.chapters_seen?.length ?? 0],
    ["Scene", scene?.id ?? "-"],
  ];

  for (const [label, value] of metrics) {
    const li = document.createElement("li");
    li.textContent = `${label}: ${value}`;
    els.statsList.appendChild(li);
  }
}

function renderPath(path) {
  els.pathList.innerHTML = "";
  const recent = (path || []).slice(-16);

  for (const step of recent) {
    const li = document.createElement("li");
    li.textContent = `${step.scene_title} -> ${step.choice_label}`;
    els.pathList.appendChild(li);
  }
}

function updateProgress(scene) {
  const ratio = Math.min(Math.max(scene?.progress?.completion_ratio || 0, 0), 1);
  const percent = Math.round(ratio * 100);
  els.progressBar.value = percent;
  els.progressLabel.textContent = `${percent}%`;
}

function persistAutosaveMarker(state) {
  if (state?.started) {
    localStorage.setItem(STORAGE_KEY, "1");
  } else {
    localStorage.removeItem(STORAGE_KEY);
  }
}

function showEndingSummary(scene, state) {
  if (!scene?.is_ending || !scene.ending) {
    return;
  }

  els.endingTitle.textContent = `${scene.ending.title} (${scene.ending.type})`;
  els.endingSummary.textContent = scene.ending.summary || "Ending reached.";
  els.endingPath.innerHTML = "";

  const pathTail = (state?.path || []).slice(-12);
  for (const step of pathTail) {
    const li = document.createElement("li");
    li.textContent = `${step.scene_title} -> ${step.choice_label}`;
    els.endingPath.appendChild(li);
  }

  els.endingModal.classList.remove("hidden");
  els.endingModal.setAttribute("aria-hidden", "false");
}

function hideEndingSummary() {
  els.endingModal.classList.add("hidden");
  els.endingModal.setAttribute("aria-hidden", "true");
}

function showSaveModal() {
  els.saveModal.classList.remove("hidden");
  els.saveModal.setAttribute("aria-hidden", "false");
}

function hideSaveModal() {
  els.saveModal.classList.add("hidden");
  els.saveModal.setAttribute("aria-hidden", "true");
}

async function refreshSaveSlots() {
  const data = await apiRequest(API.saves);
  els.saveSlotList.innerHTML = "";

  if (!data.slots || data.slots.length === 0) {
    const empty = document.createElement("li");
    empty.textContent = "No saves found.";
    els.saveSlotList.appendChild(empty);
    return;
  }

  data.slots.forEach((slot) => {
    const li = document.createElement("li");
    const button = document.createElement("button");
    button.className = "btn btn-secondary btn-small";
    button.textContent = `Load ${slot.saved_at}`;
    button.addEventListener("click", async () => {
      await loadSlot(slot.slot_id);
      hideSaveModal();
    });

    li.textContent = `${slot.slot_id.slice(0, 8)}... `;
    li.appendChild(button);
    els.saveSlotList.appendChild(li);
  });
}

async function renderSceneAndState(scene, state) {
  uiState.latestScene = scene;
  uiState.latestState = state;

  showGameScreen();
  animateSceneSwap();

  els.hudChapter.textContent = scene.chapter;
  els.hudSceneTitle.textContent = scene.title;

  els.sceneTags.innerHTML = "";
  (scene.tags || []).forEach((tag) => {
    els.sceneTags.appendChild(createTagPill(tag));
  });

  await renderSceneText(scene.text || []);
  renderChoices(scene.choices || []);

  renderInventory(state.inventory || {});
  renderStats(state, scene);
  renderPath(state.path || []);
  updateProgress(scene);

  persistAutosaveMarker(state);

  if (scene.is_ending) {
    showEndingSummary(scene, state);
  }
}

async function startGame() {
  hideEndingSummary();
  setButtonsDisabled(true);

  try {
    const data = await apiRequest(API.start, { method: "POST" });
    await renderSceneAndState(data.scene, data.state);
    els.titleStatus.textContent = "Run started.";
  } catch (error) {
    alert(`Could not start game: ${error.message}`);
  } finally {
    setButtonsDisabled(false);
  }
}

async function continueGame() {
  setButtonsDisabled(true);

  try {
    const data = await apiRequest(API.state);
    if (!data.scene) {
      showTitleScreen("No active run found. Start a new game.");
      return;
    }
    await renderSceneAndState(data.scene, data.state);
  } catch (error) {
    alert(`Could not continue game: ${error.message}`);
  } finally {
    setButtonsDisabled(false);
  }
}

async function onChoice(choiceId) {
  if (uiState.typingInProgress) {
    return;
  }

  setButtonsDisabled(true);
  try {
    hideEndingSummary();
    const data = await apiRequest(API.choice, {
      method: "POST",
      body: { choice_id: choiceId },
    });
    await renderSceneAndState(data.scene, data.state);
  } catch (error) {
    alert(`Choice failed: ${error.message}`);
  } finally {
    setButtonsDisabled(false);
  }
}

async function restartGame() {
  if (!window.confirm("Restart your current run?")) {
    return;
  }

  setButtonsDisabled(true);
  try {
    await apiRequest(API.restart, { method: "POST" });
    hideEndingSummary();
    showTitleScreen("Run reset. Ready for a new opening move.");
    localStorage.removeItem(STORAGE_KEY);
  } catch (error) {
    alert(`Could not restart: ${error.message}`);
  } finally {
    setButtonsDisabled(false);
  }
}

async function saveRun() {
  setButtonsDisabled(true);
  try {
    const data = await apiRequest(API.save, { method: "POST" });
    alert(`Saved successfully. Slot: ${data.slot.slot_id.slice(0, 8)}...`);
  } catch (error) {
    alert(`Save failed: ${error.message}`);
  } finally {
    setButtonsDisabled(false);
  }
}

async function loadSlot(slotId) {
  setButtonsDisabled(true);
  try {
    hideEndingSummary();
    const data = await apiRequest(API.load, {
      method: "POST",
      body: { slot_id: slotId },
    });

    if (!data.scene) {
      showTitleScreen("Loaded slot has no active scene. Start again.");
      return;
    }

    await renderSceneAndState(data.scene, data.state);
  } catch (error) {
    alert(`Load failed: ${error.message}`);
  } finally {
    setButtonsDisabled(false);
  }
}

async function openLoadModal() {
  try {
    await refreshSaveSlots();
    showSaveModal();
  } catch (error) {
    alert(`Could not list saves: ${error.message}`);
  }
}

function bindEvents() {
  els.btnStart.addEventListener("click", startGame);
  els.btnContinue.addEventListener("click", continueGame);
  els.btnLoadMenu.addEventListener("click", openLoadModal);

  els.btnSave.addEventListener("click", saveRun);
  els.btnLoad.addEventListener("click", openLoadModal);
  els.btnRestart.addEventListener("click", restartGame);

  els.btnCloseModal.addEventListener("click", hideSaveModal);

  els.btnEndingRestart.addEventListener("click", async () => {
    hideEndingSummary();
    await startGame();
  });

  els.btnEndingClose.addEventListener("click", hideEndingSummary);

  els.saveModal.addEventListener("click", (event) => {
    if (event.target === els.saveModal) {
      hideSaveModal();
    }
  });

  els.endingModal.addEventListener("click", (event) => {
    if (event.target === els.endingModal) {
      hideEndingSummary();
    }
  });
}

async function bootstrap() {
  bindEvents();

  // Title screen state hint.
  const marker = localStorage.getItem(STORAGE_KEY);
  if (marker) {
    els.titleStatus.textContent = "Saved progress detected. Continue is available.";
  }

  try {
    const data = await apiRequest(API.state);
    if (data.scene) {
      els.titleStatus.textContent = "Active run detected on this browser session.";
      els.btnContinue.disabled = false;
    }
  } catch (error) {
    // Non-fatal startup issue: keep app interactive.
    // eslint-disable-next-line no-console
    console.error("State bootstrap failed", error);
  }
}

bootstrap();
