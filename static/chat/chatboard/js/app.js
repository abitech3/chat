$(document).ready(function () {

    /*--------------------------------------------------------------
    SEARCHBAR START
    --------------------------------------------------------------*/
    var sp = document.querySelector('.iconbox-search');
    var searchbar = document.querySelector('.iconbox-searchbar');
    var shclose = document.querySelector('.search-close');
  
    function changeClass() {
      searchbar.classList.add('search-visible');
    }
  
    function closesearch() {
      searchbar.classList.remove('search-visible');
    }
    sp.addEventListener('click', changeClass);
    shclose.addEventListener('click', closesearch);
    /*--------------------------------------------------------------
    SEARCHBAR END
    --------------------------------------------------------------*/
  
  
    /*--------------------------------------------------------------
    TOOLTIP START
    --------------------------------------------------------------*/
    $('[data-toggle="tooltip"]').tooltip()
    /*--------------------------------------------------------------
    TOOLTIP END
    --------------------------------------------------------------*/
  
  
    /*--------------------------------------------------------------
    CAROUSAL START
    --------------------------------------------------------------*/
    $('.owl-carousel').owlCarousel({
      loop: false,
      margin: 2,
      nav: false,
      items: 4
    })
    /*--------------------------------------------------------------
    CAROUSAL END
    --------------------------------------------------------------*/
  
    /*--------------------------------------------------------------
    PERFECT SCROLLBAR START
    --------------------------------------------------------------*/
    var selectors = ['.sidebar-userlist', '.sidebar-contactlist', '.conversation-panel__body', '.information-panel__body', '.ca-call-details-history', '.ca-content__contactstab', '.modal-contact-list', '.profile-settings-list'];
    selectors.forEach(function (selector) {
      $(selector).each(function () {
        const ps = new PerfectScrollbar($(this)[0], {
          suppressScrollX: true
        });
        ps.isRtl = false;
        ps.update();
      });
    });
    /*--------------------------------------------------------------
    PERFECT SCROLLBAR END
    --------------------------------------------------------------*/
  
  
    /*--------------------------------------------------------------
    INFORMATION PANEL START
    --------------------------------------------------------------*/
  
    $(".personalinfo-panel-opener").on('click', function () {
      $("body").addClass("info-panel-opened");
      $(".backdrop-overlay").removeClass("hidden");
      $(".theme-customizer").removeClass("active");
    });
    $(".groupinfo-panel-opener").on('click', function () {
      $("body").addClass("info-panel-opened");
      $(".backdrop-overlay").removeClass("hidden");
    });
    $(".information-panel__closer").on('click', function () {
      $("body").removeClass("info-panel-opened");
      $(".backdrop-overlay").addClass("hidden");
    });
    /*--------------------------------------------------------------
    INFORMATION PANEL END
    --------------------------------------------------------------*/
  
  
    /*--------------------------------------------------------------
    SETTINGS PANEL START
    --------------------------------------------------------------*/
  
    $(function () {
      var $window = $(window),
        $body = $('.settings-nav-menu .nav .nav-link');
  
      function resize() {
        if ($window.width() < 768) {
          return $body.removeClass('active');
        }
      }
  
      $window
        .resize(resize)
        .trigger('resize');
    })
    /*--------------------------------------------------------------
    SETTINGS PANEL END
    --------------------------------------------------------------*/
  
  
    /*--------------------------------------------------------------
    MODAL START
    --------------------------------------------------------------*/
    $(".dialpad-opener").on('click', function () {
      $(".modal-contact-list").toggle();
      $(".modal-dialpad").toggle();
      $(this).find(".mdi").toggleClass("mdi-dialpad mdi-account-multiple-outline");
    });
    $(".new-group-dialog .iconbox").on('click', function () {
      $(this).toggleClass("btn-solid-info btn-solid-success")
      $(this).find(".iconbox__icon").toggleClass("mdi-plus mdi-check");
    });
    /*--------------------------------------------------------------
    MODAL END
    --------------------------------------------------------------*/
  
  
    /*--------------------------------------------------------------
    DEMO CHAT JQUERY START
    --------------------------------------------------------------*/
  
    //chats Tab Inside
    $("#caChatsTab").on('click', function () {
      $(".ca-content__callstab, .ca-content__contactstab").hide();
      $(".ca-content__chatstab").show();
    });
  
    $("#personal-chat-tab").on('click', function () {
      if ($("#personal-chat .conversation").hasClass("active")) {
        $(".ca-content__chatstab--group").hide();
        $(".ca-content__chatstab--personal").show();
      } else {
        $(".ca-content__chatstab--personal, .ca-content__chatstab--group").hide();
      }
    });
    $("#groups-chat-tab").on('click', function () {
      if ($("#groups-chat .conversation").hasClass("active")) {
        $(".ca-content__chatstab--group").show();
        $(".ca-content__chatstab--personal").hide();
      } else {
        $(".ca-content__chatstab--personal, .ca-content__chatstab--group").hide();
      }
    });
  
    //Calls Tab Inside
    $("#caCallsTab").on('click', function () {
      $(".ca-content__chatstab, .ca-content__contactstab").hide();
      if ($(".calllist").hasClass("active")) {
        $(".ca-content__callstab").show();
      } else {
        $(".ca-content__callstab").hide();
      }
    });
  
    // Contacts Tab Inside
    $("#caContactsTab").on('click', function () {
      $(".ca-content__chatstab, .ca-content__callstab").hide();
      if ($(".contactlist").hasClass("active")) {
        $(".ca-content__contactstab").show();
      } else {
        $(".ca-content__contactstab").hide();
      }
    });
  
    /*--------------------------------------------------------------
    DEMO CHAT JQUERY END
    --------------------------------------------------------------*/
  
  
    /*--------------------------------------------------------------
     RESPONSIVE START
    --------------------------------------------------------------*/
  
    $(function () {
      var $window = $(window),
        $body = $('body');
  
      function resize() {
        if ($window.width() < 992) {
          $(".conversation, .calllist, .contactlist").removeClass("active");
          $("#personal-chat .conversation").on('click', function () {
            $(this).addClass("active");
            $(".ca-content__chatstab--personal").show();
            $(".ca-content-wrapper").addClass("open");
          });
          $("#groups-chat .conversation").on('click', function () {
            $(this).addClass("active");
            $(".ca-content__chatstab--group").show();
            $(".ca-content-wrapper").addClass("open");
          });
          $("#caCalls .calllist").on('click', function () {
            $(this).addClass("active");
            $(".ca-content__callstab").show();
            $(".ca-content-wrapper").addClass("open");
          });
          $("#caContacts .contactlist").on('click', function () {
            $(this).addClass("active");
            $(".ca-content__contactstab").show();
            $(".ca-content-wrapper").addClass("open");
          });
          $(".conversation-panel__back-button").on('click', function () {
            $(".ca-content-wrapper").removeClass("open");
            $(".conversation, .calllist, .contactlist").removeClass("active");
          });
          return $body.addClass('small-devices');
        }
      }
  
      $window
        .resize(resize)
        .trigger('resize');
    })
  
  
    /*--------------------------------------------------------------
     RESPONSIVE END
    --------------------------------------------------------------*/
    /*--------------------------------------------------------------
    MFB EVENT START
    --------------------------------------------------------------*/
    $(function () {
  
      var $win = $(window); // or $box parent container
      var $box = $("#mfbMenu");
  
      $win.on("click.Bst", function (event) {
        if (
          $box.has(event.target).length == 0 //checks if descendants of $box was clicked
          &&
          !$box.is(event.target) //checks if the $box itself was clicked
        ) {
          $("#mfbMenu").attr('data-mfb-state', "close")
        }
      });
  
    });
    /*--------------------------------------------------------------
    MFB EVENT END
    --------------------------------------------------------------*/
  
    /*--------------------------------------------------------------
     SWITCH BETWEEN THEMES START
    --------------------------------------------------------------*/
    var themes = "light-default-theme light-purple-theme light-pink-theme light-green-theme light-red-theme light-orange-theme light-blue-theme light-darkblue-theme light-lightpink-theme dark-default-theme dark-purple-theme dark-pink-theme dark-green-theme dark-red-theme dark-orange-theme dark-blue-theme dark-darkblue-theme dark-lightpink-theme";
    $('[data-theme]').click(function () {
      $('[data-theme]').removeClass("selected");
      $(this).addClass("selected");
      $('body').removeClass(themes);
      $('body').addClass($(this).attr('data-theme'));
    });
  
    //RTL Layout
    $(".rtlSwitch").change(function () {
      $("body").toggleClass("rtl");
    });
  
    $(".theme-customizer-opener").on("click", function() {
      $(this).parents('.theme-customizer').toggleClass("active");
    });
     /*--------------------------------------------------------------
     SWITCH BETWEEN THEMES END
    --------------------------------------------------------------*/
     /*--------------------------------------------------------------
    SEARCH START
    --------------------------------------------------------------*/
    $('#userSearch').bind('keyup', function() {
      var searchString = $(this).val();
      $(".userSearchList li").each(function(index, value) {
          currentName = $(value).text()
          if( currentName.toUpperCase().indexOf(searchString.toUpperCase()) > -1) {
              $(value).show();
          } else {
              $(value).hide();
          }
      });
    });
  
  
  
    // $('.search-close').click(function(){
    //     $('#userSearch').val(null)
    // });
  
  
  
     /*--------------------------------------------------------------
     SEARCH END
    --------------------------------------------------------------*/

    const msgerForm = get(".msger-inputarea");
    const msgerInput = get(".msger-input");
    const msgerChat = get(".chatstyle-01");
    // const msgerForm =  document.getElementsByClassName('msger-inputarea');
    // const msgerInput  = document.getElementsByClassName('msger-input');
    // const msgerChat  =  document.getElementsByClassName('msger-chat');
    
    
    const BOT_MSGS = [
      "Hi, how are you?",
      "I am not Human , so i dont have name but you can call me Bolt!",
      "I like to play games... But I don't know how to play!",
      "Sorry if my answers are not relevant. :))",
      "I feel sleepy! :("
    ];
    
    // Icons made by Freepik from www.flaticon.com
    const BOT_IMG = "{{bot.bot_image.url}}";
    const PERSON_IMG = "{{request.user.user_image.url}}";
    const BOT_NAME = "{{bot.bot_name}}";
    const PERSON_NAME = "{{request.user.first_name}}";
    
    msgerForm.addEventListener("submit", event => {
      event.preventDefault();
    
      var msgText = msgerInput.value.trim();
      if (msgText.lenght === 0){
          return ;
        } 
    
     
      appendMessage("send", msgText, PERSON_IMG);
    
      getUserResponse(msgText);
      //  botResponse();
    
      msgerInput.value = "";
    
      
    
    });
    
    // function appendMessage(name, img, side, text) {
    //   //   Simple solution for small apps
    //   const msgHTML = `
    //     <div class="msg ${side}-msg">
    //       <div class="msg-img" style="background-image: url(${img})"></div>
    
    //       <div class="msg-bubble">
    //         <div class="msg-info">
    //           <div class="msg-info-name">${name}</div>
    //           <div class="msg-info-time">${formatDate(new Date())}</div>
    //         </div>
    
    //         <div class="msg-text">${text}</div>
    //       </div>
    //     </div>
    //   `;
    
    //   msgerChat.insertAdjacentHTML("beforeend", msgHTML);
    //   msgerChat.scrollTop += 500;
    // }


    function appendMessage(side, text , img){

      const msgHTML = `<div class="ca-${side}">
      <div class="ca-${side}__msg-group">
          <div class="ca-${side}__msgwrapper">
              <div class="ca-msg-actions">
                  <div class="iconbox-dropdown dropdown">
                      <div class="iconbox btn-hovered-light" id="dropdownMenuButtons1"  role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                          <i class="iconbox__icon mdi mdi-dots-horizontal"></i>
                      </div>
                      <div class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenuButtons1">
                          
                          <a class="dropdown-item" href="javascript:;">
                              <span><i class="mdi mdi-share-outline"></i></span> 
                              <span>Forward</span>
                          </a>
                          <a class="dropdown-item" href="javascript:;">
                              <span><i class="mdi mdi-content-copy"></i></span> 
                              <span>Copy</span>
                          </a>
                          <a class="dropdown-item" href="javascript:;">
                              <span><i class="mdi mdi-star-outline"></i></span> 
                              <span>Add Star</span>
                          </a>
                          <a class="dropdown-item" href="javascript:;">
                              <span><i class="mdi mdi-trash-can-outline"></i></span> 
                              <span>Delete</span>
                          </a>
                      </div>
                  </div>
              </div>
              <div class="ca-${side}__msg">${text}</div>
          </div>
          <div class="metadata">
              <span class="time">${formatDate(new Date())}</span>
              <span class="tick">
                  <img src="assets/images/tick/tick-read.svg" alt="">
              </span>
          </div>
      </div>
     
      <div class="user-avatar user-avatar-sm user-avatar-rounded online">
          <img src="${img}" alt="">
      </div>
  </div>`
      ;

      msgerChat.insertAdjacentHTML("beforeend", msgHTML);
      msgerChat.scrollTop += 500;
    }
    
    function botResponse() {
      const r = random(0, BOT_MSGS.length - 1);
      const msgText = BOT_MSGS[r];
      const delay = msgText.split(" ").length * 100;
    
      setTimeout(() => {
        appendMessage("received",msgText , PERSON_IMG );
      }, delay);
    }
    
    // Utils
    function get(selector, root = document) {
      return root.querySelector(selector);
    }
    
    function formatDate(date) {
      const h = "0" + date.getHours();
      const m = "0" + date.getMinutes();
    
      return `${h.slice(-2)}:${m.slice(-2)}`;
    }
    
    function random(min, max) {
      return Math.floor(Math.random() * (max - min) + min);
    }
    
     function getUserResponse(userText){
    
      const csrfToken = $('input[name=csrfmiddlewaretoken]').val();
       
      $.ajax({
        url: "chat",
        type: "POST",
        data: {
         'message': userText
        },
        headers: {
          'X-CSRFToken': csrfToken  // Include the CSRF token in the headers
        },
        success: function(result) {
          const response = result.response;
          print(response);
          setTimeout(() => {
            appendMessage("received", response, BOT_IMG);
          }, 3000);
        }
    
      });
    
    }




  
  });