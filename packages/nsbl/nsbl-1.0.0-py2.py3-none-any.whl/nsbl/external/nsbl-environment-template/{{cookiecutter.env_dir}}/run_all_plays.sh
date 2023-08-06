#!/usr/bin/env bash

THIS_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if [ -e "$HOME/.nix-profile/etc/profile.d/nix.sh" ]; then source "$HOME/.nix-profile/etc/profile.d/nix.sh"; fi

# additional bin paths
{% for path in cookiecutter.extra_paths.split(':') %}
if [ -d "{{ path }}" ]; then
    export PATH="{{ path }}:$PATH"
fi
{% endfor %}

cd "${THIS_DIR}/plays"

{{cookiecutter.extra_script_commands}}

# read vault_pw
PW_FILE="vault_pw"
VAULT_FILE="run_vault.yml"
#mkfifo "${PW_FILE}"
#echo "${vault_pw}" >"${PW_FILE}" &

ANSIBLE_CONFIG=./ansible.cfg ansible-playbook --vault-id=freckles_run@${PW_FILE} --extra-vars=@${VAULT_FILE} {{cookiecutter.ansible_playbook_args}} {{cookiecutter.ask_sudo}} {{cookiecutter.playbook}} 2>&1

rm -f "${PW_FILE}"
rm -f "${VAULT_FILE}"
