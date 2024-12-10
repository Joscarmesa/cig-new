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
    var currentOpenInfoBox = null;
  
    enfermedadesItems.forEach(function (item) {
      item.addEventListener("click", function () {
        var infoBox = this.querySelector(".enfermedad-info");
  
        // Cerrar la caja de información actualmente abierta si existe
        if (currentOpenInfoBox && currentOpenInfoBox !== infoBox) {
          currentOpenInfoBox.style.display = "none";
        }
  
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
  
          // Actualizar la caja de información actualmente abierta
          currentOpenInfoBox = infoBox;
        }
      });
    });
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


document.addEventListener("DOMContentLoaded", function () {
  // Variables generales
  const form = document.getElementById("form-cita");
  const contactoChecks = document.querySelectorAll('input[name="contacto"]');
  const referidoSi = document.getElementById("referido_si");
  const referidoNo = document.getElementById("referido_no");
  const referidoNombre = document.getElementById("referido_nombre");
  const flashMessages = document.getElementById("flash-messages");

  // Mostrar/ocultar campos según el método de contacto seleccionado
  contactoChecks.forEach(function (check) {
      check.addEventListener("change", function () {
          const inputId = this.id + "-input";
          const inputField = document.getElementById(inputId);

          if (this.checked) {
              inputField.style.display = "block";
              inputField.required = true; // Hace el campo obligatorio
          } else {
              inputField.style.display = "none";
              inputField.required = false; // Quita la obligación del campo
              inputField.value = ""; // Limpia el valor si se deselecciona
          }

          // Asegurarse de que solo un método esté seleccionado
          contactoChecks.forEach(function (otherCheck) {
              if (otherCheck !== check) {
                  otherCheck.checked = false;
                  const otherInputField = document.getElementById(otherCheck.id + "-input");
                  if (otherInputField) {
                      otherInputField.style.display = "none";
                      otherInputField.required = false;
                      otherInputField.value = ""; // Limpia el campo
                  }
              }
          });
      });
  });

  // Manejar mostrar/ocultar campo de "Referido por médico"
  if (referidoSi && referidoNo && referidoNombre) {
      referidoSi.addEventListener("change", function () {
          if (referidoSi.checked) {
              referidoNo.checked = false; // Desmarcar "No"
              referidoNombre.style.display = "block";
              referidoNombre.required = true; // Hace el campo obligatorio
          }
      });

      referidoNo.addEventListener("change", function () {
          if (referidoNo.checked) {
              referidoSi.checked = false; // Desmarcar "Sí"
              referidoNombre.style.display = "none";
              referidoNombre.required = false; // Quita la obligación
              referidoNombre.value = ""; // Limpia el campo
          }
      });
  }

  // Validar formulario antes del envío
  form.addEventListener("submit", function (event) {
      let isValid = true;

      // Validar que al menos un método de contacto esté seleccionado y su campo no esté vacío
      const contactoSeleccionado = Array.from(contactoChecks).some(function (check) {
          const inputField = document.getElementById(check.id + "-input");
          if (check.checked) {
              if (inputField && inputField.value.trim() === "") {
                  alert(`Por favor, completa el campo para ${check.value}`);
                  inputField.focus();
                  isValid = false;
              }
              return true;
          }
          return false;
      });

      if (!contactoSeleccionado) {
          alert("Por favor, selecciona al menos un método de contacto y completa el campo correspondiente.");
          isValid = false;
      }

      // Validar que el nombre del médico esté lleno si fue referido
      if (referidoSi && referidoSi.checked && referidoNombre.value.trim() === "") {
          alert("Por favor, completa el campo del nombre del médico que te refirió.");
          referidoNombre.focus();
          isValid = false;
      }

      // Si hay alguna validación fallida, detener el envío
      if (!isValid) {
          event.preventDefault();
          return;
      }

      // Enviar formulario con fetch para manejar mensajes flash
      event.preventDefault(); // Previene el refresco de la página
      const formData = new FormData(form);

      fetch("/solicitar-cita", {
          method: "POST",
          body: formData,
      })
          .then((response) => response.json()) // Suponiendo que el servidor devuelve JSON
          .then((data) => {
              // Limpiar mensajes previos
              flashMessages.innerHTML = "";

              // Mostrar el mensaje flash
              const alertDiv = document.createElement("div");
              alertDiv.className = `alert alert-${data.success ? "success" : "danger"}`;
              alertDiv.textContent = data.message;
              flashMessages.appendChild(alertDiv);

              // Si es exitoso, limpiar el formulario
              if (data.success) {
                  form.reset();

                  // Ocultar y limpiar campos de contacto
                  contactoChecks.forEach(function (check) {
                      const inputField = document.getElementById(check.id + "-input");
                      if (inputField) {
                          inputField.style.display = "none";
                          inputField.value = "";
                      }
                  });

                  // Ocultar y limpiar campo de referido
                  referidoNombre.style.display = "none";
                  referidoNombre.value = "";
              }
          })
          .catch((error) => {
              console.error("Error al enviar el formulario:", error);
              flashMessages.innerHTML = `
                  <div class="alert alert-danger">Error al procesar la solicitud.</div>
              `;
          });
  });
});



//FIN DEL CUESTIONARIO



// FUNCION PARA NAVBAR
$(document).ready(function () {
    var timer;
    var lastScrollTop = 0; // Variable para almacenar la última posición de desplazamiento
  
    function showNavbar() {
      $('.navbar').removeClass('navbar-hidden');
      clearTimeout(timer);
    }
  
    function hideNavbar() {
      timer = setTimeout(function () {
        $('.navbar').addClass('navbar-hidden');
      }, 3000);
    }
  
    // Mostrar la barra de navegación al pasar el ratón por la parte superior de la pantalla
    $(window).mousemove(function (e) {
      if (e.clientY <= 50) {
        showNavbar();
      }
    });
  
    // Ocultar la barra de navegación si el usuario se desplaza hacia abajo y mostrarla si se desplaza hacia arriba
    $(window).scroll(function () {
      var currentScrollTop = $(this).scrollTop(); // Obtener la posición actual de desplazamiento
  
      if (currentScrollTop < lastScrollTop) {
        // Si se desplaza hacia arriba
        showNavbar();
      } else {
        // Si se desplaza hacia abajo
        hideNavbar();
      }
  
      lastScrollTop = currentScrollTop; // Actualizar la última posición de desplazamiento
    });
  
    // Iniciar el temporizador para ocultar la barra de navegación
    hideNavbar();
  });

// Asegúrate de que la barra de navegación esté visible al cambiar el tamaño de la ventana
$(window).resize(function() {
  if ($(window).width() <= 768) {
    showNavbar(); // Mostrar la barra de navegación en dispositivos móviles
  }
});

// Mostrar la barra de navegación si el ancho de la ventana es <= 768px
if ($(window).width() <= 768) {
  showNavbar();
};