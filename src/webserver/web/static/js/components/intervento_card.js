const template = document.createElement("template");
template.innerHTML = `
    <style>
        * {
            margin: 0;
            padding: 0;
        }
        .intervento_card {
            max-width: 400px;
            width: 100%;
            user-select: none;
        }
        
        .intervento_card .top {
            background-color: #272732;
            width: 100%;
            height: 60px;
            border-radius: 12px 12px 0 0;
        
            display: flex;
            flex-direction: row;
            align-items: center;
        }

        .top .intervento_p {
            flex: 0.2;

            margin-right: 15px;
            font-size: 20px;
            font-weight: bold;

            margin-left: 25px;
        }

        .top .dynamic_intervento_title {
            flex: 0.8;
            text-align: left;
        }
        
        .intervento_card .center,
        .intervento_card .bottom {
            background-color: #21212b;
        }
        
        .icon_wrapper {
            width: 20%;
            height: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        .nav_icon {
            width: 25px;
            height: 25px;
            border-radius: 10px;
            margin: auto;
            margin-top: 15px;
            background-color: transparent;

            display: flex;
            align-items: center;
            justify-content: center;
        }

        .nav_icon svg {
            width: 100%;
            height: 100%;
        }
        
        .text {
            width: 80%;
            margin-top: 18px;
        }
        
        .top p ::slotted(p) {
            font-size: 20px;
            font-weight: bold;
        }
        
        .intervento_card .center .container {
            display: flex;
            flex-direction: row;
            height: 70px;
        }
        
        .intervento_card .center .container .text, .intervento_card .center .container .text ::slotted(p) {
            font-size: 16px;
            font-weight: 300;
        }
        
        
        .intervento_card .bottom {
            width: 100%;
            height: 50px;
            border-radius: 0 0 12px 12px;
            border-top: 1px solid rgba(103, 111, 119, 0.5);
        
            text-align: center;
            font-weight: 300;
            font-size: 16px;
        
            cursor: pointer;
        }
        
        .intervento_card .bottom p, .intervento_card .bottom::slotted(p) {
            margin-top: 10px;
        }
    </style>
    <div class="intervento_card">
        <div class="top">
            <div class="intervento_p">
                <p>Intervento: </p>
            </div>
            <div class="dynamic_intervento_title">
                <slot name="titolo">
                    <p>lorem  ipsum</p>
                </slot>
            </div>
        </div>
        <div class="center">
            <div class="container">
                <div class="icon_wrapper">
                    <div class="nav_icon">
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-clock" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <circle cx="12" cy="12" r="9" />
                            <polyline points="12 7 12 12 15 15" />
                        </svg>
                    </div>
                </div>
                <div class="text">
                    <slot name="data">
                        <p>lorem ipsum</p>
                    </slot>
                </div>
            </div>
            <div class="container">
                <div class="icon_wrapper">
                    <div class="nav_icon">
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-notes" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <rect x="5" y="3" width="14" height="18" rx="2" />
                            <line x1="9" y1="7" x2="15" y2="7" />
                            <line x1="9" y1="11" x2="15" y2="11" />
                            <line x1="9" y1="15" x2="13" y2="15" />
                        </svg>
                    </div>
                </div>
                <div class="text">
                    <slot name="note">
                        <p>lorem ipsum</p>
                    </slot>
                </div>
            </div>
            <div class="container">
                <div class="icon_wrapper">
                    <div class="nav_icon">
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-building-cottage" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <line x1="3" y1="21" x2="21" y2="21" />
                            <path d="M4 21v-11l2.5 -4.5l5.5 -2.5l5.5 2.5l2.5 4.5v11" />
                            <circle cx="12" cy="9" r="2" />
                            <path d="M9 21v-5a1 1 0 0 1 1 -1h4a1 1 0 0 1 1 1v5" />
                        </svg>
                    </div>
                </div>
                <div class="text">
                    <slot name="sede">
                        <p>lorem ipsum</p>
                    </slot>
                </div>
            </div>
            <div class="container">
                <div class="icon_wrapper">
                    <div class="nav_icon">
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-subtask" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <line x1="6" y1="9" x2="12" y2="9" />
                            <line x1="4" y1="5" x2="8" y2="5" />
                            <path d="M6 5v11a1 1 0 0 0 1 1h5" />
                            <rect x="12" y="7" width="8" height="4" rx="1" />
                            <rect x="12" y="15" width="8" height="4" rx="1" />
                        </svg>
                    </div>
                </div>
                <div class="text">
                    <slot name="att">
                        <p>lorem ipsum</p>
                    </slot>
                </div>
            </div>
            <div class="container">
                <div class="icon_wrapper">
                    <div class="nav_icon">
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-user" width="20" height="20" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <circle cx="12" cy="7" r="4" />
                            <path d="M6 21v-2a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4v2" />
                        </svg>
                    </div>
                </div>
                <div class="text">
                    <slot name="utente">
                        <p>lorem ipsum</p>
                    </slot>
                </div>
            </div>
        </div>
        <div class="bottom">
            <p>
                <svg width="28" height="28" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M4.66667 8.16667H23.3333" stroke="#FF2825" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M11.6667 12.8333V19.8333" stroke="#FF2825" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M16.3333 12.8333V19.8333" stroke="#FF2825" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M5.83333 8.16667L7 22.1667C7 22.7855 7.24583 23.379 7.68341 23.8166C8.121 24.2542 8.71449 24.5 9.33333 24.5H18.6667C19.2855 24.5 19.879 24.2542 20.3166 23.8166C20.7542 23.379 21 22.7855 21 22.1667L22.1667 8.16667" stroke="#FF2825" stroke-linecap="round" stroke-linejoin="round"/>
                    <path d="M10.5 8.16667V4.66667C10.5 4.35725 10.6229 4.0605 10.8417 3.84171C11.0605 3.62292 11.3572 3.5 11.6667 3.5H16.3333C16.6428 3.5 16.9395 3.62292 17.1583 3.84171C17.3771 4.0605 17.5 4.35725 17.5 4.66667V8.16667" stroke="#FF2825" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>            
            </p>
        </div>
    </div>
`;

export class InterventoCard extends HTMLElement {
    constructor() {
        super();
        const shadowRoot = this.attachShadow({ mode: "open" });
        // clone template content nodes to the shadow DOM
        shadowRoot.appendChild(template.content.cloneNode(true));
    }
}

window.customElements.define("intervento-card", InterventoCard);
