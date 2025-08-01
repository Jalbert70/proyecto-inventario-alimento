# Guía de Colaboración en Proyecto con GitHub y VS Code

Esta guía explica paso a paso cómo trabajar de forma colaborativa en un proyecto de código usando Git y GitHub desde Visual Studio Code (VS Code).

## 💻 Requisitos Iniciales

- Tener instalado **Git**: [https://git-scm.com/](https://git-scm.com/)
- Tener una cuenta en **GitHub**: [https://github.com/](https://github.com/)
- Tener instalado **Visual Studio Code**: [https://code.visualstudio.com/](https://code.visualstudio.com/)

---

## 🚀 Primera vez que se suma al proyecto

1. **Abre VS Code**
2. **Abre la terminal** (Ctrl + ñ o desde el menú Terminal > Nuevo terminal)
3. Ve a la carpeta donde quieres guardar el proyecto:

```bash
cd Desktop
```

4. **Clona el repositorio:**

```bash
git clone https://github.com/Jalbert70/proyecto-inventario-alimento.git
```

5. Entra a la carpeta del proyecto:

```bash
cd proyecto-inventario-alimento
```

---

## ✅ Antes de empezar a trabajar

> Esto evita conflictos con cambios hechos por otros.

```bash
git pull
```

---

## 📂 Editar archivos

- Puedes trabajar directamente desde VS Code.
- Asegúrate de **guardar los archivos** que edites.

---

## ⬆️ Subir tus cambios al proyecto (GitHub)

1. Agrega los archivos modificados:

```bash
git add .
```

2. Crea un mensaje de confirmación:

```bash
git commit -m "Agrega nueva funcionalidad de clima"
```

3. Sube los cambios a GitHub:

```bash
git push
```

---

## 📆 Buenas prácticas

- Siempre hacer `git pull` al comenzar a trabajar.
- Siempre hacer `git push` al terminar para compartir tu trabajo.
- No editar el mismo archivo al mismo tiempo que otra persona.
- Comentar bien los códigos y mantener un orden.

---

## 🚩 Problemas comunes

| Error                                        | Solución                                                                    |
| -------------------------------------------- | --------------------------------------------------------------------------- |
| `error: src refspec main does not match any` | No hiciste `git commit` antes de `push`.                                    |
| `Merge conflict`                             | Alguien editó lo mismo que tú. Revisa el archivo y soluciona manualmente.   |
| `Permission denied`                          | Asegúrate de tener acceso al repositorio o haber iniciado sesión en GitHub. |

---

## 📖 Recomendado

- Usar la extensión **GitLens** en VS Code para ver los cambios y el historial.
- Puedes trabajar desde varios computadores si sigues los mismos pasos con `git pull` y `git push`.

---

## ✉️ Dudas

Si tienes alguna duda, pregúntale al responsable del proyecto o revisa la documentación oficial de Git: [https://git-scm.com/docs](https://git-scm.com/docs)

