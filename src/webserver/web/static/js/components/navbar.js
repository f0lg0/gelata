const template = document.createElement("template");
template.innerHTML = `
    <style>
        #navbar {
            width: 100%;
            height: 64px;
            background-color: #21212b;
            position: fixed;

            display: flex;
            flex-direction: row;
        }

        .left {
            width: calc(100% - 235px);
        }

        .home {
            width: 200px;
            height: 100%;

            display: flex;
            flex-direction: row;

            margin-left: 7%;
            cursor: pointer;
        }

        .icon {
            width: 20%;
            height: 100%;

            display: flex;
            align-items: center;
        }

        .icon svg {
            margin: auto;
        }

        .home p {
            margin: auto;
            margin-left: 10px;

            font-weight: bold;
            font-size: 20px;
        }

        .right {
            width: 235px;

            display: flex;
            flex-direction: row;

        }

        .logout_btn_container {
            width: 100%;

            display: flex;
            align-items: center;
        }

        .logout_btn {
            width: 70%;
            height: 35px;
            margin: auto;

            border: 1px solid #E76363;
            border-radius: 12px;
            display: flex;
            align-items: center;

            cursor: pointer;
        }

        .logout_btn p {
            text-align: center;
            margin: auto;
            color: #E76363;
            font-size: 14px;
        }

        .profile_container {
            width: 100%;

            display: flex;
            align-items: center;
        }

        .profile_img {
            width: 42px;
            height: 42px;
            margin: auto;

            background-color: #DE9191;
            border-radius: 25px;
            cursor: pointer;
        }

        .profile_img img {
            width: 100%;
            height: 100%;
            border-radius: 25px;
        }

        @media only screen and (max-width: 500px) {
            .logout_btn_container {
                display: none;
            }

            .left {
                width: 80%;
            }
            .right {
                width: 20%;
            }
        }
    </style>
    <div id="navbar">
        <div class="left">
            <div class="home" onclick="routeHome()">
                <div class="icon">
                    <svg width="35" height="35" viewBox="0 0 35 35" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M27.7083 5.83331H7.29165C6.48623 5.83331 5.83331 6.48623 5.83331 7.29165V10.2083C5.83331 11.0137 6.48623 11.6666 7.29165 11.6666H27.7083C28.5137 11.6666 29.1666 11.0137 29.1666 10.2083V7.29165C29.1666 6.48623 28.5137 5.83331 27.7083 5.83331Z" fill="white" stroke="white" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M13.125 17.5H7.29165C6.48623 17.5 5.83331 18.1529 5.83331 18.9583V27.7083C5.83331 28.5137 6.48623 29.1667 7.29165 29.1667H13.125C13.9304 29.1667 14.5833 28.5137 14.5833 27.7083V18.9583C14.5833 18.1529 13.9304 17.5 13.125 17.5Z" fill="white" stroke="white" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M20.4167 17.5H29.1667" stroke="white" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M20.4167 23.3333H29.1667" stroke="white" stroke-linecap="round" stroke-linejoin="round"/>
                        <path d="M20.4167 29.1667H29.1667" stroke="white" stroke-linecap="round" stroke-linejoin="round"/>
                    </svg>
                </div>
                <p>Dashboard</p>
            </div>
        </div>
        <div class="right">
            <div class="logout_btn_container">
                <div class="logout_btn" onclick="logout()">
                    <p>Logout</p>
                </div>
            </div>
            <div class="profile_container" onclick="routeToProfile()">
                <div class="profile_img">
                    <img id="profile_pic" src="" />
                </div>
            </div>
        </div>
    </div>
`;

export class Navbar extends HTMLElement {
    constructor() {
        super();
        const shadowRoot = this.attachShadow({ mode: "open" });
        // clone template content nodes to the shadow DOM
        shadowRoot.appendChild(template.content.cloneNode(true));
    }
}

window.customElements.define("navbar-component", Navbar);

const profile_pic_el = document.querySelector("body > navbar-component").shadowRoot.querySelector("#profile_pic");

export { profile_pic_el };
