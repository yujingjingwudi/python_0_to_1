$(function(){
	var $slide = $('.slide_con');
	var $li = $('.slide li');
	var $li_len = $li.length;
	var $point = $('.point');
	var $prior = $('.prior');
	var $after = $('.after');
	var $now_page = 0;
	var $prev_page = 0;
	//开关，防止暴力操作
	var $switch = false;
	// 除了第一个
	$li.not(':first').css({
		'left': '-760px'
	});
	for(var i=0;i<$li_len;i++)
	{
		var $new_li = $('<li>');
		if(i==0){
			$new_li.addClass('active');
		}

		// $new_li.appendTo($point);
		$point.append($new_li);
	}

	var $pointli = $('.point li');

	//自动播放,通常放在大容器里
	var timer = setInterval(auto_move,3000);

	$slide.mouseenter(function(event) {
		/* Act on the event */
		clearInterval(timer);
	});

	$slide.mouseleave(function(event) {
		/* Act on the event */
		timer = setInterval(auto_move,3000);
	});


	$('.point li').click(function(event) {
		/* Act on the event */
		$now_page = $(this).index();
		move();
		$(this).addClass('active').siblings().removeClass('active');
	});

	//prior按钮
	$prior.click(function(event) {
		/* Act on the event */
		if($switch==true){
			return;
		}
		$switch = true;
		$now_page--;
		move();
		$pointli.eq($now_page).addClass('active').siblings().removeClass('active');
	});

	$after.click(function(event) {
		/* Act on the event */
		if($switch==true){
			return;
		}
		$switch = true;
		$now_page++;
		move();
		$pointli.eq($now_page).addClass('active').siblings().removeClass('active');
	});

	function auto_move(){
		$now_page++;
		move();
		$pointli.eq($now_page).addClass('active').siblings().removeClass('active');
	}


	function move(){
		if($now_page<0){
			$now_page = $li_len-1;
			$li.eq($now_page).css({'left': -760});
			$li.eq($now_page).animate({'left':0});
			$li.eq($prev_page).animate({'left':760},function(){
				$switch = false;
			});
			$prev_page = $now_page;
			return;
		}


		if($now_page>$li_len-1){
			$now_page = 0;
			$li.eq($now_page).css({'left': 760});
			$li.eq($now_page).animate({'left':0});
			$li.eq($prev_page).animate({'left':-760},function(){
				$switch = false;
			});
			$prev_page = $now_page;
			return;
		}

		// alert($now_page);

		if($now_page>$prev_page){
			 $li.eq($now_page).css({'left': 760});
			 // $li.eq($now_page).animate({'left':0});
			 $li.eq($prev_page).animate({'left':-760});
			 $prev_page = $now_page;
		}
		if($now_page<$prev_page){
			 $li.eq($now_page).css({'left': -760});
			 // $li.eq($now_page).animate({'left':0});
			 $li.eq($prev_page).animate({'left':760});
			 $prev_page = $now_page;
		}
		$li.eq($now_page).animate({'left':0},function(){
			$switch = false;
		});

	}	
})