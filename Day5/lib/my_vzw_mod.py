#!/usr/bin/python

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

RETURN = """
original message:
    description: The original name param that was passed in
    type: str
message:
    description: The output message that our module will produce
"""

# Must for ANY module you want to run i Ansible
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        name=dict(type="str", required=True),
        new=dict(type="bool", required=False, default=False),
    )

    # This is the json that will be sent BACK to ansible
    result = dict(
            changed=False, 
            original_message="", 
            message=""
    )

    # AnsibleModule is the class that was imported
    module = AnsibleModule(
            argument_spec=module_args, 
            supports_check_mode=True
    )

    # If in check mode (true) then return the dict above
    if module.check_mode:
        return result

    # We are past check.mode, set the result key original_message to
    # module (AnsibleModule above) which ponts to arguents_spec who
    # points to module_args of 'name'
    result["original_message"] = module.params["name"]
    result["message"] = "Welcome to class, " + module.params["name"]

    # When it was called, the user actually set the new value
    # as opposed to taking default
    if module.params["new"]:
        result["changed"] = True

    # Invoke an AnsibleModule method called fail_json with a message
    # The **result means argument unpacking.
    # AnsibleModule.fail_json will get the msg, and then ALL of the result dict
    if module.params["name"] == "fail_me":
        module.fail_json(msg="you requested the module to fail :(", **result)

    module.exit_json(**result)


# Define main to actually run run_module()
def main():
    run_module()


# Prevent the import statement from actually running the command
if __name__ == "__main__":
    main()
