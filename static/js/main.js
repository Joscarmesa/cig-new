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
              inputField.required = true;
          } else {
              inputField.style.display = "none";
              inputField.required = false;
              inputField.value = "";
          }

          // Asegurarse de que solo un método esté seleccionado
          contactoChecks.forEach(function (otherCheck) {
              if (otherCheck !== check) {
                  otherCheck.checked = false;
                  const otherInputField = document.getElementById(otherCheck.id + "-input");
                  if (otherInputField) {
                      otherInputField.style.display = "none";
                      otherInputField.required = false;
                      otherInputField.value = "";
                  }
              }
          });
      });
  });

  // Manejar mostrar/ocultar campo de "Referido por médico"
  if (referidoSi && referidoNo && referidoNombre) {
      referidoSi.addEventListener("change", function () {
          if (referidoSi.checked) {
              referidoNo.checked = false;
              referidoNombre.style.display = "block";
              referidoNombre.required = true;
          }
      });

      referidoNo.addEventListener("change", function () {
          if (referidoNo.checked) {
              referidoSi.checked = false;
              referidoNombre.style.display = "none";
              referidoNombre.required = false;
              referidoNombre.value = "";
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

      if (referidoSi && referidoSi.checked && referidoNombre.value.trim() === "") {
          alert("Por favor, completa el campo del nombre del médico que te refirió.");
          referidoNombre.focus();
          isValid = false;
      }

      if (!isValid) {
          event.preventDefault();
          return;
      }

      // Enviar formulario con fetch
      event.preventDefault();
      const formData = new FormData(form);
      const csrfToken = document.querySelector('input[name="csrf_token"]').value;

      fetch("/solicitar-cita", {
          method: "POST",
          headers: {
              "X-CSRFToken": csrfToken, // Agrega el token CSRF en el encabezado
          },
          body: formData,
      })
          .then((response) => response.json())
          .then((data) => {
              flashMessages.innerHTML = "";

              const alertDiv = document.createElement("div");
              alertDiv.className = `alert alert-${data.success ? "success" : "danger"}`;
              alertDiv.textContent = data.message;
              flashMessages.appendChild(alertDiv);

              if (data.success) {
                  form.reset();
                  contactoChecks.forEach(function (check) {
                      const inputField = document.getElementById(check.id + "-input");
                      if (inputField) {
                          inputField.style.display = "none";
                          inputField.value = "";
                      }
                  });
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
