#!/usr/bin/env bash

PLAY_DIR=${1}

VAULT_FILE_NAME="run_vault.yml"

PW_FILE="vault_pw"
UV_FILE="unencrypted_vault"

cd "${PLAY_DIR}"

{% for path in cookiecutter.extra_paths.split(':') %}
if [ -d "{{ path }}" ]; then
    export PATH="{{ path }}:$PATH"
fi
{% endfor %}

#document="---\n"
#
## read the password and document
#while read
#do
#   if [ -z "${pw}" ]
#   then
#      pw="${REPLY}"
#   else
#      document="${document}\n${REPLY}"
#   fi
#done
#
## creating the named pipes
#mkfifo "${PW_FILE}"
#mkfifo "${UV_FILE}"
#
## filling the pipes
#echo "${pw}" >"${PW_FILE}" &
#printf -- "${document}" >"${UV_FILE}" &

# creating the encrypted vault
ansible-vault encrypt --vault-id freckles_run@${PW_FILE} --output "${VAULT_FILE_NAME}" "${UV_FILE}"

exit_code=$?

# deleting the pipes
rm "${PW_FILE}"
rm "${UV_FILE}"

exit $exit_code
