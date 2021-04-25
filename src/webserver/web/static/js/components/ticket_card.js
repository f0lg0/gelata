const template = document.createElement("template");
template.innerHTML = `
    <style>
        * {
            margin: 0;
            padding: 0;
        }
        .ticket_card {
            max-width: 400px;
            width: 100%;
            user-select: none;
        }
        
        .ticket_card .top {
            background-color: #272732;
            width: 100%;
            height: 60px;
            border-radius: 12px 12px 0 0;
        
            display: flex;
            flex-direction: row;
        }
        
        .ticket_card .center,
        .ticket_card .bottom {
            background-color: #21212b;
        }
        
        .icon_wrapper {
            width: 20%;
            height: 100%;
        }
        
        .icon {
            width: 30px;
            height: 30px;
            border-radius: 10px;
            background-color: #df2e59;
            margin: auto;
            margin-top: 15px;
        }
        
        .text {
            width: 80%;
            height: 100%;
            margin-top: 18px;
        }
        
        .top .text p, .top .text ::slotted(p) {
            font-size: 20px;
            font-weight: bold;
        }
        
        .ticket_card .center .container {
            display: flex;
            flex-direction: row;
            height: 70px;
        }
        
        .ticket_card .center .container .text, .ticket_card .center .container .text ::slotted(p) {
            font-size: 16px;
            font-weight: 300;
        }
        
        .ticket_card .center .container .icon {
            background-color: transparent;
            border: 2px solid purple;
            width: 25px;
            height: 25px;
        }
        
        .ticket_card .bottom {
            width: 100%;
            height: 50px;
            border-radius: 0 0 12px 12px;
            border-top: 1px solid rgba(103, 111, 119, 0.5);
        
            text-align: center;
            font-weight: 300;
            font-size: 16px;
        
            cursor: pointer;
        }
        
        .ticket_card .bottom p, .ticket_card .bottom::slotted(p) {
            margin-top: 10px;
        }
    </style>
    <div class="ticket_card">
        <div class="top">
            <div class="icon_wrapper">
                <div class="icon"></div>
            </div>
            <div class="text">
                <slot name="titolo">
                    <p>Titolo</p>
                </slot>
            </div>
        </div>
        <div class="center">
            <div class="container">
                <div class="icon_wrapper">
                    <div class="icon"></div>
                </div>
                <div class="text">
                    <slot name="campo_0">
                        <p>lorem ipsum</p>
                    </slot>
                </div>
            </div>
            <div class="container">
                <div class="icon_wrapper">
                    <div class="icon"></div>
                </div>
                <div class="text">
                    <slot name="campo_1">
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

export class TicketCard extends HTMLElement {
    constructor() {
        super();
        const shadowRoot = this.attachShadow({ mode: "open" });
        // clone template content nodes to the shadow DOM
        shadowRoot.appendChild(template.content.cloneNode(true));
    }
}

window.customElements.define("ticket-card", TicketCard);
