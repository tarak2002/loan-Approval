const sign_in_btn = document.querySelector('#sign-in-button');
const sign_up_btn = document.querySelector('#sign-up-button');
const container = document.querySelector('.container');
sign_up_btn.addEventListener('click', ()=>{
    container.classList.add('sign-up-mode');
});
sign_in_btn.addEventListener('click', ()=>{
    container.classList.remove('sign-up-mode');
});
//https://storyset.com/illustration/computer-login/amico    https://www.youtube.com/watch?v=I5_T547tHf0
//https://uicookies.com/free-bank-website-templates/    https://themewagon.com/themes/free-bootstrap-4-html5-professional-business-website-template-sierra/ https://bfotool.com/website-download-online
//https://themewagon.com/themes/free-bootstrap-4-html5-cryptocurrency-website-template-crypto/  https://uicookies.com/free-bank-website-templates/