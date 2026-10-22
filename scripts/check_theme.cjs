// Exercise preference behavior without a browser or third-party dependencies.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const source = fs.readFileSync(path.join(__dirname, "../theme.js"), "utf8");

function visit({ dark = false, saved = null, blocked = false } = {}) {
  const root = { dataset: {} };
  const events = {};
  const button = {
    hidden: true,
    attrs: {},
    setAttribute(key, value) {
      this.attrs[key] = value;
    },
    addEventListener(key, callback) {
      events[key] = callback;
    },
  };
  const meta = {
    setAttribute(key, value) {
      this[key] = value;
    },
  };
  const media = {
    matches: dark,
    addEventListener(key, callback) {
      this.change = callback;
    },
  };
  let stored = saved;
  let loaded;
  vm.runInNewContext(source, {
    document: {
      documentElement: root,
      querySelector(selector) {
        return selector === ".theme-toggle" ? button : meta;
      },
      addEventListener(key, callback) {
        loaded = callback;
      },
    },
    window: {
      matchMedia() {
        return media;
      },
    },
    localStorage: {
      getItem() {
        if (blocked) throw new Error("Storage blocked");
        return stored;
      },
      setItem(key, value) {
        if (blocked) throw new Error("Storage blocked");
        stored = value;
      },
    },
  });
  return {
    root,
    button,
    meta,
    stored: () => stored,
    load: () => loaded(),
    click: () => events.click(),
    system(value) {
      media.matches = value;
      media.change();
    },
  };
}

const automatic = visit();
assert.equal(
  automatic.root.dataset.theme,
  "light",
  "Theme is set before DOMContentLoaded",
);
automatic.load();
assert.equal(automatic.button.hidden, false);
automatic.system(true);
assert.equal(
  automatic.root.dataset.theme,
  "dark",
  "Follow system changes before an explicit choice",
);
assert.equal(automatic.button.attrs["aria-pressed"], "true");
assert.equal(automatic.meta.content, "#111318");
automatic.click();
assert.equal(automatic.root.dataset.theme, "light");
assert.equal(automatic.stored(), "light");
automatic.system(true);
assert.equal(
  automatic.root.dataset.theme,
  "light",
  "System changes must not override the visitor",
);
assert.equal(
  visit({ dark: true, saved: automatic.stored() }).root.dataset.theme,
  "light",
  "Remember the selected theme on a later visit",
);

const savedDark = visit({ saved: "dark" });
savedDark.load();
assert.equal(savedDark.root.dataset.theme, "dark");
assert.equal(savedDark.button.attrs["aria-pressed"], "true");
savedDark.click();
assert.equal(savedDark.button.attrs["aria-pressed"], "false");
assert.equal(savedDark.meta.content, "#ffffff");

assert.equal(visit({ dark: true }).root.dataset.theme, "dark");
assert.equal(
  visit({ dark: true, saved: "invalid" }).root.dataset.theme,
  "dark",
  "Ignore invalid saved values",
);
const restricted = visit({ dark: true, blocked: true });
restricted.load();
restricted.click();
assert.equal(
  restricted.root.dataset.theme,
  "light",
  "Toggle works even when storage reads and writes throw",
);
console.log(
  "PASS: automatic theme, system changes, explicit preference, persistence, toggle state, browser color, invalid storage and blocked storage",
);
