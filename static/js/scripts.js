function onDelete(id, app) {
    let txt = "";
    switch (app) {
        case 'pedidos':
            txt = "Estás seguro de eliminar el pedido?";
            break;
        case 'productos':
            txt = "Estás seguro de eliminar el producto?";
            break;
        case 'clientes':
            txt = "Estás seguro de eliminar el cliente?";
            break;
        default:
            return alert("app no válida.")
    }

    Swal.fire({
        title: txt,
        text: "Esta acción no se puede revertir",
        icon: "warning",
        showCancelButton: true,
        background: "#f1f5f9",
        confirmButtonColor: "#f56565",
        cancelButtonColor: "#c6c9cb",
        confirmButtonText: "Si, eliminar",
        cancelButtonText: "Cancelar"
    }).then(async (result) => {
        if (result.isConfirmed) {
            try {
                const res = await fetch(`http://127.0.0.1:8000/dashboard/${app}/eliminar/${id}`)
                const data = await res.json()

                if (!res.ok) {
                    throw data
                }

                let timerInterval;
                Swal.fire({
                    title: `${data.msg}`,
                    timer: 2000,
                    icon: "success",
                    timerProgressBar: true,
                    showConfirmButton: false,
                    willClose: () => {
                        clearInterval(timerInterval);
                    }
                }).then((result) => {
                    window.location.reload()
                });

            } catch (err) {
                let timerInterval;
                Swal.fire({
                    title: `${err.msg ? err.msg : "Error al eliminar"}`,
                    timer: 3000,
                    icon: "error",
                    timerProgressBar: true,
                    showConfirmButton: false,
                    willClose: () => {
                        clearInterval(timerInterval);
                    }
                })
            }
        }
    });
}