# --- Tu código original y perfecto ---
tareas_prioritarias = ["cp01", "cp02", "cp03"]
detalles_tareas = {
    "cp01": {"descripcion": "Hacer la tarea de Python", "asignado_a": "Juan"},
    "cp02": {"descripcion": "Enviar el informe", "asignado_a": "Luis"},
    "cp03": {"descripcion": "Revisar el codigo", "asignado_a": "Ana"}
}  # (Nota: Puse los strings directamente para que sea más fácil de leer)

# --- La mejora de legibilidad ---

# 1. Obtenemos el ID de la próxima tarea de forma clara
id_proxima_tarea = tareas_prioritarias[0]

# 2. Usamos ese ID para obtener TODOS los detalles de esa tarea en una sola variable
info_tarea = detalles_tareas[id_proxima_tarea]

# 3. Ahora el print es mucho más limpio y fácil de leer
print(
    f"La proxima tarea prioritaria es '{info_tarea['descripcion']}', y está asignada a {info_tarea['asignado_a']}.")
