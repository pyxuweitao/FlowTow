% rebase('base.tpl')

<div class="header">
    <div class="am-g">
        <h1>FlowTow</h1>
        <p><br/>post digital images and comment</p>
    </div>
    <hr/>
</div>
<div class="am-g">
    <div class="am-u-lg-6 am-u-md-8 am-u-sm-centered">
        {{ registerInfo }}
        %if showRegister:
        <form method="post" class="am-form" action="/registerSubmit" onsubmit="return valid()">
            <label for="nick">nickname:</label>
            <input type="text" name="nick" id="nick" placeholder="Enter your nick name" value="">
            <br>
            <label for="password">Password:</label>
            <input type="password" name="password" id="password" placeholder="Enter your password" value="">
            <br>
            <label for="passwordRepeated">Repeat Password:</label>
            <input type="password" name="passwordRepeated" id="passwordRepeated" placeholder="Repeat your password" value="">
            <br>

            <div class="am-cf">
                <input id="register" type="submit" name="" value="Register" class="am-btn am-btn-sm am-fl">
            </div>
        </form>
        %end
        <hr>
        <p>© 2016 FlowTow</p>
    </div>
</div>