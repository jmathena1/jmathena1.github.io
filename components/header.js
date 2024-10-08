class Header extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
        <br>
        <header class="website-header">
            <b class="homepage-title">
            JOHN W. MATHENA
            </b>
            <nav>
                <ul class="nav-bar-menu">
                    <li id="about-link" class="nav-bar-item">
                        <a href="index.html" class="nav-bar-link">About</a>
                    </li>
                    <li id="portfolio-link" class="nav-bar-item">
                        <a href="portfolio.html" class="nav-bar-link">Portfolio</a>
                    </li>
                    <li id="resume-link" class="nav-bar-item">
                        <a href="resume.html" target="_blank" class="nav-bar-link">
                        Resume
                        </a>
                    </li>
                    <li id="wiki-link" class="nav-bar-item">
                        <a href="wiki-pages/wiki.html" class="nav-bar-link">Wiki</a>
                    </li>
                </ul>
            </nav>
            <div>
                <a href="https://www.linkedin.com/in/johnwmathena" target="_blank">
                    <img id="social-media-photo" src="photos/linkedin.png">
                </a>
                <a href="https://www.github.com/jmathena1" target="_blank">
                    <img id="social-media-photo" src="photos/github-black.png">
                </a>
                <a href="https://www.twitter.com/JohnMathena6" target="_blank">
                    <img id="social-media-photo" src="photos/twitter.png">
                </a>
                <a href="https://www.instagram.com/mathenajohn/" target="_blank">
                    <img id="social-media-photo" src="photos/instagram-logo.png">
                </a>
            </div>
	    </header>
        <br>
    `;
    }

  }

customElements.define('header-component', Header);
