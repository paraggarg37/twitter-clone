(function(){


    var tweetTemplate = $('#tweetTemplate').html();
    var searchTemplate =$('#searchTemplate').html();
    var user_tweetTemplate = $('#user-tweetTemplate').html();

    var tpl = _.template(tweetTemplate);
    var stpl = _.template(searchTemplate);
    var utpl = _.template(user_tweetTemplate);

    var $tweets = $('#tweets');


    function loadTweets(){

        var data = "user="+ $tweets.data("user");
        var tweets = $tweets.data("tweets");
            data+="&tweets="+tweets
        $.ajax({
            url:"/tweets",
            data:data,
            dataType:"json",
            type:"GET",
            success:function(res){
                console.log(r = JSON.parse(res));
                var tweets = JSON.parse(res);
                //console.log( tpl({"data":tweets}) );

                var html = "";
                tweets.forEach(function(tweet){
                    console.log(tweet.fields.tweet);
                    html+= tpl({"data":tweet});
                })

                $tweets.append(html);
            }
        })
    }

    var post = $('#post_tweet');

    function updateTweet(){

        var val = post.val();
        var data ="tweet="+val;
        if(post.val()!="") {

            $.ajax({
                url: "/tweet",
                data: data,
                type: "POST",
                success: function () {
                    console.log("tweet posted");

                    var html = utpl({"post":val});

                    $(html).hide().prependTo($tweets).fadeIn('slow');

                    post.val('');
                }
            })
        }
    }

    var $followingContainer = $('#following-container')
    var $followersContainer = $('#followers-container')
    function loadFollowing(){

        var data = "user="+ $tweets.data("user");

        $.ajax({
            url:"/following",
            data:data,
            type:"GET",
            success:function(res){
                console.log(JSON.parse(res));
                var result = JSON.parse(res);

                var html = "";
                    result.forEach(function(data){

                        html+= stpl({"data":data});

                    })

                    $followingContainer.html(html);
            }
        })



    }

    function loadFollowers(){

        var data = "user="+ $tweets.data("user");

        $.ajax({
            url:"/followers",
            data:data,
            type:"GET",
            success:function(res){
                console.log(JSON.parse(res));
                var result = JSON.parse(res);

                var html = "";
                    result.forEach(function(data){

                        html+= stpl({"data":data});

                    })

                    $followersContainer.html(html);
            }
        })



    }
    if($followingContainer.length >0) {
            loadFollowing();
            loadFollowers()
    }

    $('#submit_tweet').click(updateTweet);
    var resultContainer = $('#search_result');

    $('#search')
        .on('keyup', _.debounce(function (e) {

        var data = this.value;
        if(data!="") {
            $.ajax({
                url: "/PeopleSearch",
                data: "query="+data,
                type:"GET",
                dataType:"json",
                success:function(res){
                    console.log(JSON.parse(res));
                    var result = JSON.parse(res);
                    var html = "";
                    result.forEach(function(data){

                        html+= stpl({"data":data});

                    })

                    resultContainer.html(html);
                }
            })
        }else{
            resultContainer.html('');
        }

    }, 200))

        .on('focus',function(){
            resultContainer.show();
        })

        $(document).on('click', function(e) {
            if($(e.target).closest('#search','#search_result').length==0){
                resultContainer.hide();
            }
        });



    $('.follow-unfollow').click(function(){
        var $this = $(this);

         var data =  "user="+$this.data("user")+"&operation="+$this.data("operation");

            $.ajax({
                url:"/followunfollow",
                data:data,
                success:function(){
                    if($this.data("operation") =="follow"){
                        $this.data("operation","unfollow");
                        $this.removeClass("btn-success").addClass("btn-danger").text("unfollow");

                    }else{
                         $this.data("operation","follow");
                         $this.addClass("btn-success").removeClass("btn-danger").text("follow");
                    }

                }
            })
    })





    loadTweets();




})()
