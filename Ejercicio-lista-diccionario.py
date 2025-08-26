tareas_prioritarias = ["cp01", "cp02", "cp03"]
detalles_tareas = {tareas_prioritarias[0]: {"descripcion": "Hacer la tarea de Python", "asignado_a": "Juan"},
                   tareas_prioritarias[1]: {"descripcion": "Enviar el informe", "asignado_a": "Luis"},
                   tareas_prioritarias[2]: {"descripcion": "Revisar el codigo", "asignado_a": "Ana"}}
print(
    f"La proxima tarea prioritaria es {detalles_tareas[tareas_prioritarias[0]]['descripcion']} asignado a {detalles_tareas[tareas_prioritarias[0]]['asignado_a']}")
