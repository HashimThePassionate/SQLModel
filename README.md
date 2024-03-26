# SQLModel

#  Lets Explore SQL Model

<p align="center">
  <a href="https://sqlmodel.tiangolo.com"><img src="https://sqlmodel.tiangolo.com/img/logo-margin/logo-margin-vector.svg" alt="SQLModel"></a>
</p>
<p align="center">
    <em>SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.</em>
</p>
<p align="center">
<a href="https://github.com/tiangolo/sqlmodel/actions?query=workflow%3ATest" target="_blank">
    <img src="https://github.com/tiangolo/sqlmodel/workflows/Test/badge.svg" alt="Test">
</a>
<a href="https://github.com/tiangolo/sqlmodel/actions?query=workflow%3APublish" target="_blank">
    <img src="https://github.com/tiangolo/sqlmodel/workflows/Publish/badge.svg" alt="Publish">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/tiangolo/sqlmodel" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/tiangolo/sqlmodel.svg" alt="Coverage">
<a href="https://pypi.org/project/sqlmodel" target="_blank">
    <img src="https://img.shields.io/pypi/v/sqlmodel?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
</p>

---

**Documentation**: <a href="https://sqlmodel.tiangolo.com" target="_blank">https://sqlmodel.tiangolo.com</a>

**Source Code**: <a href="https://github.com/tiangolo/sqlmodel" target="_blank">https://github.com/tiangolo/sqlmodel</a>

---

SQLModel is a library for interacting with <abbr title='Also called "Relational databases"'>SQL databases</abbr> from Python code, with Python objects. It is designed to be intuitive, easy to use, highly compatible, and robust.

**SQLModel** is based on Python type annotations, and powered by <a href="https://pydantic-docs.helpmanual.io/" class="external-link" target="_blank">Pydantic</a> and <a href="https://sqlalchemy.org/" class="external-link" target="_blank">SQLAlchemy</a>.

The key features are:

* **Intuitive to write**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging. Designed to be easy to use and learn. Less time reading docs.
* **Easy to use**: It has sensible defaults and does a lot of work underneath to simplify the code you write.
* **Compatible**: It is designed to be compatible with **FastAPI**, Pydantic, and SQLAlchemy.
* **Extensible**: You have all the power of SQLAlchemy and Pydantic underneath.
* **Short**: Minimize code duplication. A single type annotation does a lot of work. No need to duplicate models in SQLAlchemy and Pydantic.
