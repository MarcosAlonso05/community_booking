# Community_booking

## Ejecución
Instalar dependencias del archivo requirements.txt
```bash
    pip install -r requirements.txt
```
Una vez instaladas las dependencias, inicia el servidor con el siguiente comando:

```bash
uvicorn app.main:app --reload
```

##Credenciales preregistradas

| Role | Username | Password | Description |
| :--- | :--- | :--- | :--- |
| **Resident** | `resident1` | `pass1` | Main user for testing reservations. |
| **Resident** | `resident2` | `pass2` | Use in Incognito Mode to test capacity limits. |
| **Admin** | `admin` | `admin` | Admin user (currently has resident privileges). |
| **Guest** | N/A | N/A | Use the **"Continue as Guest"** button. |

---

## Enlace al repositorio

```
https://github.com/MarcosAlonso05/community_booking
```
