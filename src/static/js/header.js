class Header extends HTMLElement {
  constructor() {
    super();
  }
  connectedCallback() {
    this.innerHTML = `
          <header class="website-header">
          <br />
          <b class="homepage-title"> JOHN W. MATHENA </b>
          <nav>
            <ul class="nav-bar-menu">
              <li id="about-link" class="nav-bar-item">
                <a href="/" class="nav-bar-link">About</a>
              </li>
              <li id="portfolio-link" class="nav-bar-item">
                <a href="/portfolio.html" class="nav-bar-link">Portfolio</a>
              </li>
              <li id="resume-link" class="nav-bar-item">
                <a href="/resume.html" class="nav-bar-link"> Resume </a>
              </li>
              <li id="wiki-link" class="nav-bar-item">
                <a href="/wiki-pages/index.html" class="nav-bar-link">Wiki</a>
              </li>
            </ul>
          </nav>
          <div>
            <a href="https://www.linkedin.com/in/johnwmathena" target="_blank"
              ><img class="social-media-photo" src="/photos/linkedin.png"
            /></a>
            <a href="https://www.github.com/jmathena1" target="_blank"
              ><img class="social-media-photo" src="/photos/github-black.png"
            /></a>
            <a href="https://blacksky.community/profile/did:plc:e5g4n36oc2bvq2aq4pxwewhr" target="_blank"
              ><img class="social-media-photo" src="/photos/bluesky.png"
            /></a>
            <a href="https://www.instagram.com/mathenajohn/" target="_blank"
              ><img class="social-media-photo" src="/photos/instagram-logo.png"
            /></a>
          </div>
        </header>
        `;
  }
}

customElements.define("custom-header", Header);
