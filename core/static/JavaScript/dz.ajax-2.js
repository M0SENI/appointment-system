function contactForm() {
    var r;
    window.verifyRecaptchaCallback = function(t) {
        $("input[data-recaptcha]").val(t).trigger("change")
    }, window.expiredRecaptchaCallback = function() {
        $("input[data-recaptcha]").val("").trigger("change")
    }, $(".dzForm").on("submit", function(t) {
        t.preventDefault(), $(".dzFormMsg").html('<div class="gen alert dz-alert alert-success">Submitting..</div>');
        var t = $(this).attr("action"),
            a = $(this).serialize(),
            e = 1 == $("input[reCaptchaEnable]").val();
        $.ajax({
            method: "POST",
            url: t,
            data: a,
            dataType: "json",
            success: function(t) {
                1 == t.status && (r = '<div class="gen alert dz-alert alert-success">' + t.msg + "</div>"), 0 == t.status && (r = '<div class="err alert dz-alert alert-danger">' + t.msg + "</div>"), $(".dzFormMsg").html(r), setTimeout(function() {
                    $(".dzFormMsg .alert").hide(1e3)
                }, 5e3), $(".dzForm")[0].reset(), e && grecaptcha.reset()
            }
        })
    }), $(document).on("submit", ".dzSubscribe", function(t) {
        t.preventDefault();
        var a = $(this),
            t = a.attr("action"),
            e = a.serialize();
        a.addClass("dz-ajax-overlay"), $.ajax({
            method: "POST",
            url: t,
            data: e,
            dataType: "json",
            success: function(t) {
                a.removeClass("dz-ajax-overlay"), 1 == t.status && (r = '<div class="gen alert dz-alert alert-success">' + t.msg + "</div>"), 0 == t.status && (r = '<div class="err alert dz-alert alert-danger">' + t.msg + "</div>"), $(".dzSubscribeMsg").html(r), setTimeout(function() {
                    $(".dzSubscribeMsg .alert").hide(0)
                }, 5e3), $(".dzSubscribe")[0].reset()
            }
        })
    }), $(".dz-load-more").on("click", function(t) {
        t.preventDefault();
        t = $(this).attr("rel");
        $.ajax({
            method: "POST",
            url: t,
            dataType: "html",
            success: function(t) {
                $(".loadmore-content").append(t)
            }
        })
    })
}
jQuery(document).ready(function() {
    contactForm()
});