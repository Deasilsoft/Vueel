import $ from "jquery";

// TODO: this doesn't currently work

$.ready(() => {
    $("html").attr("lang", eel.C("language"));
    $("body > noscript").html(eel.T("no javascript"))
});
