(function ($) {
  "use strict";

  // Spinner
  var spinner = function () {
    setTimeout(function () {
      if ($("#spinner").length > 0) {
        $("#spinner").removeClass("show");
      }
    }, 1);
  };
  spinner();

  // Initiate the wowjs
  new WOW().init();

  // Sticky Navbar
  $(window).scroll(function () {
    if ($(this).scrollTop() > 40) {
      $(".navbar").addClass("sticky-top");
    } else {
      $(".navbar").removeClass("sticky-top");
    }
  });

  // Dropdown on mouse hover
  const $dropdown = $(".dropdown");
  const $dropdownToggle = $(".dropdown-toggle");
  const $dropdownMenu = $(".dropdown-menu");
  const showClass = "show";

  $(window).on("load resize", function () {
    if (this.matchMedia("(min-width: 992px)").matches) {
      $dropdown.hover(
        function () {
          const $this = $(this);
          $this.addClass(showClass);
          $this.find($dropdownToggle).attr("aria-expanded", "true");
          $this.find($dropdownMenu).addClass(showClass);
        },
        function () {
          const $this = $(this);
          $this.removeClass(showClass);
          $this.find($dropdownToggle).attr("aria-expanded", "false");
          $this.find($dropdownMenu).removeClass(showClass);
        }
      );
    } else {
      $dropdown.off("mouseenter mouseleave");
    }
  });

  // Back to top button
  $(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
      $(".back-to-top").fadeIn("slow");
    } else {
      $(".back-to-top").fadeOut("slow");
    }
  });
  $(".back-to-top").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 1500, "easeInOutExpo");
    return false;
  });

  // Date and time picker
  $(".date").datetimepicker({
    format: "L",
  });
  $(".time").datetimepicker({
    format: "LT",
  });

  // Image comparison
  $(".twentytwenty-container").twentytwenty({});

  // ensayos carousel
  $(".ensayos-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1500,
    margin: 45,
    dots: false,
    loop: true,
    nav: true,
    navText: [
      '<i class="bi bi-arrow-left"></i>',
      '<i class="bi bi-arrow-right"></i>',
    ],
    responsive: {
      0: {
        items: 1,
      },
      768: {
        items: 2,
      },
    },
  });

  // Testimonials carousel
  $(".especialistas-carousel").owlCarousel({
    autoplay: true,
    smartSpeed: 1000,
    items: 1,
    dots: false,
    loop: true,
    nav: true,
    navText: [
      '<i class="bi bi-arrow-left"></i>',
      '<i class="bi bi-arrow-right"></i>',
    ],
  });
})(jQuery);

// Agregando funcion a la parte de enfermedades

document.addEventListener("DOMContentLoaded", function () {
  var enfermedadesItems = document.querySelectorAll(".enfermedades-item");

  enfermedadesItems.forEach(function (item) {
    item.addEventListener("click", function () {
      var infoBox = this.querySelector(".enfermedad-info");

      // Alternar la visualización de la caja de información
      if (infoBox.style.display === "block") {
        infoBox.style.display = "none";
      } else {
        infoBox.style.display = "block";

        // Ajustar la posición si es necesario
        var rect = infoBox.getBoundingClientRect();
        var windowHeight = window.innerHeight;

        if (rect.bottom > windowHeight) {
          infoBox.style.top = "auto";
          infoBox.style.bottom = "100%";
        } else {
          infoBox.style.top = "100%";
          infoBox.style.bottom = "auto";
        }
      }
    });
  });
});

// Agregando funcion a la parte de enfermedades para moviles
document.addEventListener("DOMContentLoaded", function () {
  if (window.innerWidth <= 768) {
    // Asumiendo que 768px es el límite para dispositivos móviles
    var enfermedadesItems = document.querySelectorAll(".enfermedades-item");

    enfermedadesItems.forEach(function (item) {
      item.addEventListener("click", function () {
        var infoBox = this.querySelector(".enfermedad-info");

        // Alternar la visualización de la caja de información
        if (infoBox.style.display === "block") {
          infoBox.style.display = "none";
        } else {
          infoBox.style.display = "block";

          // Ajustar la posición si es necesario
          var rect = infoBox.getBoundingClientRect();
          var windowHeight = window.innerHeight;

          if (rect.bottom > windowHeight) {
            infoBox.style.top = "auto";
            infoBox.style.bottom = "100%";
          } else {
            infoBox.style.top = "100%";
            infoBox.style.bottom = "auto";
          }
        }
      });
    });
  }
});

// AGREGANDO FUNCION A TRATAMIENTOS
document.addEventListener("DOMContentLoaded", function() {
    var hamburgers = document.querySelectorAll('.treatment-hamburger');

    hamburgers.forEach(function(hamburger) {
        hamburger.addEventListener('click', function() {
            var treatmentItem = this.parentNode.querySelector('.treatment-item p');
            if (treatmentItem.style.display === 'none' || treatmentItem.style.display === '') {
                treatmentItem.style.display = 'block';
            } else {
                treatmentItem.style.display = 'none';
            }
        });
    });
});
// AGREGANDO BOTON MOSTRAR-OCULTAR TRATAMIENTOS
document.addEventListener("DOMContentLoaded", function() {
    var toggleButton = document.querySelector('.toggle-treatments');
    var treatmentSection = document.querySelector('.treatment-section');

    toggleButton.addEventListener('click', function() {
        if (treatmentSection.style.display === 'none' || treatmentSection.style.display === '') {
            treatmentSection.style.display = 'block';
            this.textContent = "Ocultar Tratamientos";
        } else {
            treatmentSection.style.display = 'none';
            this.textContent = "Mostrar Tratamientos";
        }
    });
});
// AGREGANDO FUNCION AL CUESTIONARIO PARA DETERMINAR EL COSTO DEL FIBROSCAN (METODO DE CONTACTO)
document.addEventListener("DOMContentLoaded", function() {
    var contactoChecks = document.querySelectorAll('input[name="contacto"]');
  
    contactoChecks.forEach(function(check) {
      check.addEventListener('change', function() {
        var inputId = this.id + '-input';
        var inputField = document.getElementById(inputId);
  
        if (this.checked) {
          inputField.style.display = 'block';
        } else {
          inputField.style.display = 'none';
          inputField.value = ''; // Limpiar el campo si se deselecciona
        }
  
        // Asegurarse de que solo se selecciona una opción
        contactoChecks.forEach(function(otherCheck) {
          if (otherCheck !== check) {
            otherCheck.checked = false;
            document.getElementById(otherCheck.id + '-input').style.display = 'none';
          }
        });
      });
    });
  });
// AGREGANDO FUNCION AL CUESTIONARIO PARA DETERMINAR EL COSTO DEL FIBROSCAN (MEDICO REFERIDO)

document.addEventListener("DOMContentLoaded", function() {
    var referidoSi = document.getElementById('referido_si');
    var referidoNo = document.getElementById('referido_no');
    var referidoNombre = document.getElementById('referido_nombre');
  
    referidoSi.addEventListener('change', function() {
      if (referidoSi.checked) {
        referidoNo.checked = false; // Desmarcar "No" si "Sí" está marcado
        referidoNombre.style.display = 'block';
      } else {
        referidoNombre.style.display = 'none';
        referidoNombre.value = ''; // Limpiar el campo si "Sí" no está marcado
      }
    });
  
    referidoNo.addEventListener('change', function() {
      if (referidoNo.checked) {
        referidoSi.checked = false; // Desmarcar "Sí" si "No" está marcado
        referidoNombre.style.display = 'none';
        referidoNombre.value = ''; // Limpiar el campo si "No" está marcado
      }
    });
});
