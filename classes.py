class SKU:
    
    def __init__(self, total_licenses, type, unlimited) -> None:
        self.total_licenses = total_licenses
        self.type = type
        self.unlimited = unlimited


class IOCAttributes:

    def __init__(self, file, url, login, scheduled_task, dll_module_load, 
                    behavioral_indicators, fds, registry, data_masking, cross_process,
                    process, headers, command_scripts, autoinstall_browser_extensions,
                    dns, ip) -> None:
        pass


class Engines:

    def __init__(self, exploits, reputation, pup, remote_shell, lateral_movement,
                    preexecution_suspicious, executables, data_files, preexecution, 
                    penetration, application_control) -> None:
        pass


class AutoFileUpload:

    def __init__(self, max_local_disk_usage_limit, max_local_disk_usage, 
                    max_daily_file_upload_limit, enabled, include_benign_files,
                    max_file_size_limit, max_file_size, max_daily_file_upload) -> None:
        pass


class Policy:

    def __init__(self, agent_notification, agent_logging_on, antitampering_on,
                    network_quarantine_on, autodecommission_days, ioc_attributes,
                    mitigation_mode, engines, autoimmune_on, user_full_name, created_at, 
                    agent_ui_on, updated_at, inherited_from, scan_new_agents,
                    ioc_supported, monitor_on_write, monitor_on_execute, auto_file_upload,
                    research_on, allow_remote_shell, mitigation_mode_suspicious, 
                    user_id, ioc, automitigation_action, snapshots_on, is_default) -> None:
        pass


class Account:

    def __init__(self, name, external_id, inherits, expiration, 
                    account_type, skus, policy, unlimited_expiration) -> None:
        self.name = name
        self.external_id = external_id
        self.inherits = inherits
        self.expiration = expiration
        self.account_type = account_type
        self.skus = skus
        self.policy = policy
        self.unlimited_expiration = unlimited_expiration