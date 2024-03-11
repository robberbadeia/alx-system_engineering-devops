# increase the limits of files opened by holberton user

exec {'fix_hard_limit':
    # modify the limit
    command => '/bin/sed -i "/^holberton hard/s/5/50000/" etc/security/limits.conf',
    # path of sed command
    path    => '/usr/local/bin/:/bin/',
}

exec {'fix_soft_limit':
    # modify the limit
    command => '/bin/sed -i "/^holberton soft/s/4/50000/" etc/security/limits.conf',
    # path of sed command
    path    => '/usr/local/bin/:/bin/',
}
