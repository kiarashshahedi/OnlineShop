const select1 = document.querySelector("#btnsearchhd");
const show1 = document.querySelector("#btnsearch");

// function hide1() {
//     select1.classList.toggle("hiden");
// }
// select1.addEventListener("click", hide1)

function unhide1() {
    show1.classList.toggle("hiden");
}
select1.addEventListener("click", unhide1)

const select2 = document.querySelector("#kia");
const show2 = document.querySelector("#kiahd");

function kia() {
    show2.classList.toggle("hiden");

}
select2.addEventListener("mouseover", kia)