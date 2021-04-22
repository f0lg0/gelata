import { profile_pic_el } from "./components/navbar.js";

const user_picture = document.querySelector("#user_pic").innerText;
profile_pic_el.src = user_picture;
