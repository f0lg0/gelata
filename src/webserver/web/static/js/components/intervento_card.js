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
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-calendar" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <rect x="4" y="5" width="16" height="16" rx="2" />
                            <line x1="16" y1="3" x2="16" y2="7" />
                            <line x1="8" y1="3" x2="8" y2="7" />
                            <line x1="4" y1="11" x2="20" y2="11" />
                            <line x1="11" y1="15" x2="12" y2="15" />
                            <line x1="12" y1="15" x2="12" y2="18" />
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
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-home-2" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <polyline points="5 12 3 12 12 3 21 12 19 12" />
                            <path d="M5 12v7a2 2 0 0 0 2 2h10a2 2 0 0 0 2 -2v-7" />
                            <rect x="10" y="12" width="4" height="4" />
                        </svg>
                    </div>
                </div>
                <div class="text">
                    <slot name="plesso">
                        <p>lorem ipsum</p>
                    </slot>
                </div>
            </div>
            <div class="container">
                <div class="icon_wrapper">
                        <div class="nav_icon">
                            <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-clock" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <circle cx="12" cy="12" r="9" />
                            <polyline points="12 7 12 12 15 15" />
                        </svg>
                    </div>
                </div>
                <div class="text">
                    <slot name="freq">
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
                        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-box" width="24" height="24" viewBox="0 0 24 24" stroke-width="1.5" stroke="#ffffff" fill="none" stroke-linecap="round" stroke-linejoin="round">
                            <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
                            <polyline points="12 3 20 7.5 20 16.5 12 21 4 16.5 4 7.5 12 3" />
                            <line x1="12" y1="12" x2="20" y2="7.5" />
                            <line x1="12" y1="12" x2="12" y2="21" />
                            <line x1="12" y1="12" x2="4" y2="7.5" />
                        </svg>
                    </div>
                </div>
                <div class="text">
                    <slot name="vano">
                        <p>lorem ipsum</p>
                    </slot>
                </div>
            </div>
            <div class="container">
                <div class="icon_wrapper">
                    <div class="nav_icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-stars" viewBox="0 0 16 16">
                            <path d="M7.657 6.247c.11-.33.576-.33.686 0l.645 1.937a2.89 2.89 0 0 0 1.829 1.828l1.936.645c.33.11.33.576 0 .686l-1.937.645a2.89 2.89 0 0 0-1.828 1.829l-.645 1.936a.361.361 0 0 1-.686 0l-.645-1.937a2.89 2.89 0 0 0-1.828-1.828l-1.937-.645a.361.361 0 0 1 0-.686l1.937-.645a2.89 2.89 0 0 0 1.828-1.828l.645-1.937zM3.794 1.148a.217.217 0 0 1 .412 0l.387 1.162c.173.518.579.924 1.097 1.097l1.162.387a.217.217 0 0 1 0 .412l-1.162.387A1.734 1.734 0 0 0 4.593 5.69l-.387 1.162a.217.217 0 0 1-.412 0L3.407 5.69A1.734 1.734 0 0 0 2.31 4.593l-1.162-.387a.217.217 0 0 1 0-.412l1.162-.387A1.734 1.734 0 0 0 3.407 2.31l.387-1.162zM10.863.099a.145.145 0 0 1 .274 0l.258.774c.115.346.386.617.732.732l.774.258a.145.145 0 0 1 0 .274l-.774.258a1.156 1.156 0 0 0-.732.732l-.258.774a.145.145 0 0 1-.274 0l-.258-.774a1.156 1.156 0 0 0-.732-.732L9.1 2.137a.145.145 0 0 1 0-.274l.774-.258c.346-.115.617-.386.732-.732L10.863.1z"/>
                        </svg>
                    </div>
                </div>
                <div class="text">
                    <slot name="prodotto">
                        <p>lorem ipsum</p>
                    </slot>
                </div>
            </div>
            <div class="container">
                <div class="icon_wrapper">
                    <div class="nav_icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-tools" viewBox="0 0 16 16">
                            <path d="M1 0 0 1l2.2 3.081a1 1 0 0 0 .815.419h.07a1 1 0 0 1 .708.293l2.675 2.675-2.617 2.654A3.003 3.003 0 0 0 0 13a3 3 0 1 0 5.878-.851l2.654-2.617.968.968-.305.914a1 1 0 0 0 .242 1.023l3.356 3.356a1 1 0 0 0 1.414 0l1.586-1.586a1 1 0 0 0 0-1.414l-3.356-3.356a1 1 0 0 0-1.023-.242L10.5 9.5l-.96-.96 2.68-2.643A3.005 3.005 0 0 0 16 3c0-.269-.035-.53-.102-.777l-2.14 2.141L12 4l-.364-1.757L13.777.102a3 3 0 0 0-3.675 3.68L7.462 6.46 4.793 3.793a1 1 0 0 1-.293-.707v-.071a1 1 0 0 0-.419-.814L1 0zm9.646 10.646a.5.5 0 0 1 .708 0l3 3a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708zM3 11l.471.242.529.026.287.445.445.287.026.529L5 13l-.242.471-.026.529-.445.287-.287.445-.529.026L3 15l-.471-.242L2 14.732l-.287-.445L1.268 14l-.026-.529L1 13l.242-.471.026-.529.445-.287.287-.445.529-.026L3 11z"/>
                        </svg>
                    </div>
                </div>
                <div class="text">
                    <slot name="attrezzatura">
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
