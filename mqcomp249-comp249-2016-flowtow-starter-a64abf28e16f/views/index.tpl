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
            <h2 class="flowtow-h2">{{imagesNumber}} Images</h2>
            <ul data-am-widget="gallery"
                class="am-gallery am-avg-sm-{{imagesNumber}} am-avg-md-{{imagesNumber}} am-avg-lg-{{imagesNumber}} am-gallery-bordered">
                % for image in imagesList:
                <li>
                    <div class="am-gallery-item flowtow">
                        <img src="/static/images/{{image.get('filename')}}" alt=""/>
                        <div class="flowtow-info">
                            <span class="am-gallery-title am-icon-sm am-icon-heart likes"> {{image.get('likes')}}</span>
                            <form action="/like" method="post">
                                <input type="hidden" name="filename" value="{{image.get('filename')}}">
                                <input type="submit"
                                       class="am-btn am-btn-xs am-btn-danger am-round flowtow-like-button" value="Like">
                            </form>
                            <hr style="float:left"/>
                            <div class="am-gallery-desc date">{{image.get('timestamp')}}</div>
                            <div class="am-gallery-desc user">{{image.get('user')}}</div>
                        </div>
                    </div>
                </li>
                % end
            </ul>
        </div>
    </div>
</div>
