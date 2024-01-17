class Footer extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
        <footer class="website-footer">
          <h3>Let's connect.</h3>
          <a href="https://www.linkedin.com/in/johnwmathena" target="_blank"><img id="social-media-photo" src="photos/linkedin.png"></a>
          <a href="https://www.github.com/jmathena1" target="_blank"><img id="social-media-photo" src="photos/github-black.png" ></a>
          <a href="https://www.twitter.com/JohnMathena6" target="_blank"><img id="social-media-photo" src="photos/twitter.png"></a>
          <a href="https://www.instagram.com/mathenajohn/" target="_blank"><img id="social-media-photo" src="photos/instagram-logo.png"></a>
        </footer>
    `;
    }

  }

customElements.define('footer-component', Footer);