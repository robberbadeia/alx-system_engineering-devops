# configuration_managment
file { '/etc/ssh/ssh_config':
  ensure  => present,
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
  content => "
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}