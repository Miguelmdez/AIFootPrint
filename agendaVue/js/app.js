// Clave con la que se guardan los contactos en el navegador (localStorage)
var CLAVE_ALMACEN = 'agenda-contactos';

// Contactos de ejemplo para la primera vez que se abre la agenda
var contactosIniciales = [
	{ id: 1, nombre: 'Ana López', email: 'ana.lopez@ejemplo.com', telefono: '600 123 456' },
	{ id: 2, nombre: 'Carlos Ruiz', email: 'carlos.ruiz@ejemplo.com', telefono: '611 234 567' },
	{ id: 3, nombre: 'Lucía Martín', email: 'lucia.martin@ejemplo.com', telefono: '622 345 678' }
];

// Devuelve los contactos guardados en el navegador o, si no hay, los de ejemplo
function cargarContactos() {
	try {
		var guardados = JSON.parse(localStorage.getItem(CLAVE_ALMACEN));
		if (Array.isArray(guardados)) {
			return guardados;
		}
	} catch (e) {
		// localStorage no disponible (modo privado, etc.): usamos los de ejemplo
	}
	return contactosIniciales.slice();
}

Vue.config.productionTip = false;

var app = new Vue({
	el: '#app',
	template: '#plantilla-agenda',
	data: {
		contactos: cargarContactos(),
		nuevo: { nombre: '', email: '', telefono: '' },
		errores: {},
		mensaje: ''
	},
	computed: {
		// true cuando los tres campos tienen algo escrito (activa el botón "Añadir")
		formularioRelleno: function () {
			return this.nuevo.nombre !== '' && this.nuevo.email !== '' && this.nuevo.telefono !== '';
		},
		textoContador: function () {
			var total = this.contactos.length;
			return total === 1 ? '1 contacto' : total + ' contactos';
		}
	},
	methods: {
		// Comprueba los campos y devuelve un objeto con los errores encontrados
		validar: function () {
			var errores = {};
			if (this.nuevo.nombre.length < 2) {
				errores.nombre = 'El nombre debe tener al menos 2 caracteres.';
			}
			if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(this.nuevo.email)) {
				errores.email = 'Escribe un email válido, por ejemplo ana@ejemplo.com.';
			}
			if (!/^\+?[0-9 ]{9,15}$/.test(this.nuevo.telefono)) {
				errores.telefono = 'Escribe un teléfono válido: solo números y espacios (mínimo 9).';
			}
			return errores;
		},
		guardarContacto: function () {
			this.errores = this.validar();
			if (Object.keys(this.errores).length > 0) {
				return;
			}
			this.contactos.push({
				id: Date.now(),
				nombre: this.nuevo.nombre,
				email: this.nuevo.email,
				telefono: this.nuevo.telefono
			});
			this.mostrarMensaje('Contacto "' + this.nuevo.nombre + '" añadido.');
			this.nuevo = { nombre: '', email: '', telefono: '' };
		},
		borrarContacto: function (indice) {
			var contacto = this.contactos[indice];
			if (confirm('¿Seguro que quieres borrar a ' + contacto.nombre + '?')) {
				this.contactos.splice(indice, 1);
			}
		},
		// Muestra un mensaje de confirmación que desaparece a los 3 segundos
		mostrarMensaje: function (texto) {
			var vm = this;
			vm.mensaje = texto;
			clearTimeout(vm.temporizador);
			vm.temporizador = setTimeout(function () {
				vm.mensaje = '';
			}, 3000);
		},
		// Convierte "600 123 456" en "tel:600123456" para que el enlace llame desde el móvil
		enlaceTelefono: function (telefono) {
			return 'tel:' + telefono.replace(/\s/g, '');
		},
		// Rellena el bloque JSON-LD "ld-contactos" del <head> con la lista actual (schema.org/ItemList)
		actualizarJsonLd: function () {
			var datos = {
				'@context': 'https://schema.org',
				'@type': 'ItemList',
				'name': 'Contactos de la agenda',
				'numberOfItems': this.contactos.length,
				'itemListElement': this.contactos.map(function (contacto, i) {
					return {
						'@type': 'ListItem',
						'position': i + 1,
						'item': {
							'@type': 'Person',
							'name': contacto.nombre,
							'email': contacto.email,
							'telephone': contacto.telefono
						}
					};
				})
			};
			// El "<" se escribe como < para que ningún texto pueda cerrar el <script> antes de tiempo
			document.getElementById('ld-contactos').textContent =
				JSON.stringify(datos, null, 2).replace(/</g, '\\u003c');
		}
	},
	watch: {
		// Cada vez que cambia la lista (añadir o borrar) se guarda en el navegador y se actualiza el JSON-LD
		contactos: {
			handler: function (lista) {
				try {
					localStorage.setItem(CLAVE_ALMACEN, JSON.stringify(lista));
				} catch (e) {
					// Si no se puede guardar, la agenda sigue funcionando sin guardar
				}
				this.actualizarJsonLd();
			},
			deep: true
		}
	},
	// Al arrancar, genera el JSON-LD con los contactos iniciales
	mounted: function () {
		this.actualizarJsonLd();
	}
});
