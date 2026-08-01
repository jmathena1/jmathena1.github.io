class Footer extends HTMLElement {
  constructor() {
    super();
  }
    connectedCallback() {
    const currentYear = new Date().getUTCFullYear();
    this.innerHTML = `
    <footer class="website-footer">
          Johnny Dot Com © 2022-${currentYear} by John Mathena is licensed under
          <a href="https://creativecommons.org/licenses/by-sa/4.0/">CC BY-SA 4.0</a>
          <img
            src="https://mirrors.creativecommons.org/presskit/icons/cc.svg"
            style="max-width: 1em; max-height: 1em; margin-left: 0.2em"
          />
          <img
            src="https://mirrors.creativecommons.org/presskit/icons/by.svg"
            style="max-width: 1em; max-height: 1em; margin-left: 0.2em"
          />
          <img
            src="https://mirrors.creativecommons.org/presskit/icons/sa.svg"
            style="max-width: 1em; max-height: 1em; margin-left: 0.2em"
          />
    `;
  }
}

customElements.define("custom-footer", Footer);
