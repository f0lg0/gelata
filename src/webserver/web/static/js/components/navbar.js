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

        .right {
            max-width: 235px;
            width: 25%;

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

        }

        .profile_img img {
            width: 100%;
            height: 100%;
            border-radius: 25px;
        }
    </style>
    <div id="navbar">
        <div class="left"></div>
        <div class="right">
            <div class="logout_btn_container">
                <div class="logout_btn" onclick="logout()">
                    <p>Logout</p>
                </div>
            </div>
            <div class="profile_container">
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

const profile_pic_el = document
    .querySelector("body > navbar-component")
    .shadowRoot.querySelector("#profile_pic");

export { profile_pic_el };
