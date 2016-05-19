(function ($) {
    'use strict';

    $(function () {
        var $fullText = $('.admin-fullText');
        $('#admin-fullscreen').on('click', function () {
            $.AMUI.fullscreen.toggle();
        });

        $(document).on($.AMUI.fullscreen.raw.fullscreenchange, function () {
            $fullText.text($.AMUI.fullscreen.isFullscreen ? '退出全屏' : '开启全屏');
        });
    });
})(jQuery);


$(function () {
    $('#doc-form-file').on('change', function () {
        var fileNames = '';
        $.each(this.files, function () {
            fileNames += '<span class="am-badge">' + this.name + '</span> ';
        });
        $('#file-list').html(fileNames);
    });
});

function valid() {
    var password = $("#password").val();
    var passwordRepeated = $("#passwordRepeated").val();
    if (password == passwordRepeated) {
        return true;
    }
    else {
        alert("The password you entered two times is not the same!");
        return false;
    }
}