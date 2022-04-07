$(document).ready(function() {
    if(navigator.userAgent.indexOf("Mobi") >= 0) {
        removetag('body');
        window.alert("컴퓨터가 아닌 기기로 접속하신 것 같습니다!\n확인 버튼을 눌르시면 챗봇 페이지로 이동합니다.");
        location.href = "../html/mobile.html";
    }
    else if(window.navigator.userAgent.match(/MSIE|Trident/) !== null) {
        removetag('body');
        window.alert("Internet Explorer는 지원하지 않습니다.\n다른 브라우저로 들어와주세요! ex) 크롬");
        window.close();
    }
    removetagtime('.load', 2000);
});

function removetag(tag) {
    let element = document.querySelector(tag);
    element.parentNode.removeChild(element);
}

function removetagtime(tag, time) {
    let element = document.querySelector(tag);
    setTimeout(function() {
        element.parentNode.removeChild(element);
    }, time);
}