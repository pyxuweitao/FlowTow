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
            %if (userNick != None) and myActive:
            <form id="uploadform" class="flowtow-h2" method="post" action="/upload" enctype="multipart/form-data">
                <div class="am-form-group am-form-file">
                    <button type="button" class="am-btn am-btn-lg">
                        <i class="am-icon-cloud-upload"></i> Upload Image
                    </button>
                    <input id="doc-form-file" type="file" name="imagefile">
                </div>
                <input type="submit" class="am-btn am-btn-lg" name="submit" value="Submit"/>
            </form>
            <div id="file-list" class="flowtow-h2"></div>
            %end
            <ul data-am-widget="gallery"
                class="am-gallery am-avg-sm-3 am-avg-md-3 am-avg-lg-3 am-gallery-bordered">
                % for image in imagesList:
                <li>
                    <div class="am-gallery-item flowtow">
                        <img src="/static/images/{{image.get('filename')}}" class="flowtow-image" alt=""/>
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
