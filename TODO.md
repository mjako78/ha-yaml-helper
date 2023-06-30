# File da sistemare nome utente

- README_EXAMPLE.md

# Altre attività

- Eliminare file README.md
- Rinominare README_EXAMPLE.md in README.md

# Workflow

## Integrations > Add integration

Se aggiungo l'helper dal menu **Integrations > Add integration** appare una dialog per inserire i valori previsti.
Alla conferma vengono chiamati in sequenze i metodi

- `config_flow.py#async_config_entry_title`
- `__init__.py#async_setup_entry`
- `sensor.py#async_setup_entry`

## Helpers > Create helper

Se aggiungo l'helper dal menu **Helpers > Create helper** ottengo lo stesso risultato del punto precedente.
