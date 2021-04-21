const template = document.createElement("template");
template.innerHTML = `
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        .ticket_card {
            width: 400px;
            height: 200px;
            margin: auto;
            margin-top: 50px;
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
        
        .top .text p, ::slotted(p) {
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
        
        .ticket_card .bottom p, .ticket_card .bottom ::slotted(p) {
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
            <p>Visualizza</p>
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
