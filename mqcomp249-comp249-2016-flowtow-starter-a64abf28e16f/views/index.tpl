% rebase('base.tpl')


<div class="welcome">
    <div class="am-g">
        <div class="am-u-lg-12">
            <h1 class="welcome-title">FlowTow</h1>
            <p class="welcome-p">
                Welcome to FlowTow
            </p>
        </div>
    </div>
</div>

<div class="flowtow-background">
    <div class="am-g am-container">
        <div class="am-u-lg-12">
            <h2 class="flowtow-h2">Three Images</h2>
            <ul data-am-widget="gallery" class="am-gallery am-avg-sm-3 am-avg-md-3 am-avg-lg-3 am-gallery-bordered">
                <li>
                    <div class="am-gallery-item flowtow">
                        <img src="/static/images/seashell.jpg" alt=""/>
                        <div class="flowtow-info">
                            <span class="am-gallery-title am-icon-sm am-icon-heart likes"> 6</span>
                            <form action="/like">
                                <input type="hidden" name="filename" value="seashell.jpg">
                                <input type="submit"
                                        class="am-btn am-btn-xs am-btn-danger am-round flowtow-like-button" value="Like">
                            </form>
                            <hr style="float:left"/>
                            <div class="am-gallery-desc date">2015-09-26</div>
                            <div class="am-gallery-desc user">ZhiyuShen</div>
                        </div>
                    </div>
                </li>
                <li>
                    <div class="am-gallery-item flowtow">
                        <img src="/static/images/cycling.jpg" alt=""/>
                        <div class="flowtow-info">
                            <span class="am-gallery-title am-icon-sm am-icon-heart likes"> 6</span>
                            <form action="/like">
                                <input type="hidden" name="filename" value="cycling.jpg">
                                <input type="submit"
                                        class="am-btn am-btn-xs am-btn-danger am-round flowtow-like-button" value="Like">
                            </form>
                            <hr style="float:left"/>
                            <div class="am-gallery-desc date">2016-09-26</div>
                            <div class="am-gallery-desc user">ZhiyuShen</div>
                        </div>
                    </div>
                </li>
                <li>
                    <div class="am-gallery-item flowtow">
                        <img src="/static/images/window.jpg" alt=""/>
                        <div class="flowtow-info">
                            <span class="am-gallery-title am-icon-sm am-icon-heart likes"> 6</span>
                            <form action="/like">
                                <input type="hidden" name="filename" value="window.jpg">
                                <input type="submit"
                                        class="am-btn am-btn-xs am-btn-danger am-round flowtow-like-button" value="Like">
                            </form>
                            <hr style="float:left"/>
                            <div class="am-gallery-desc date">2014-09-26</div>
                            <div class="am-gallery-desc user">ZhiyuShen</div>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
    </div>
</div>
