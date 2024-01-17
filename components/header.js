class Header extends HTMLElement {
    constructor() {
      super();
    }

    connectedCallback() {
        this.innerHTML = `
        <header class="website-header">
            <b class="homepage-title">
            JOHN W. MATHENA
            </b>
            <nav>
                <ul class="nav-bar-menu">
                    <li id="about-link" class="nav-bar-item">
                        <a href="index.html" class="nav-bar-link">About</a>
                    </li>
                    <li id="blogs-link" class="nav-bar-item">
                        <a href="blogs.html" class="nav-bar-link">Writing</a>
                    </li>
                    <li id="portfolio-link" class="nav-bar-item">
                        <a href="portfolio.html" class="nav-bar-link">Portfolio</a>
                    </li>
                    <li id="wiki-link" class="nav-bar-item">
                        <a href="wiki.html" class="nav-bar-link">Wiki</a>
                    </li>
                </ul>
            </nav>
	    </header>
    `;
    }

  }

customElements.define('header-component', Header);