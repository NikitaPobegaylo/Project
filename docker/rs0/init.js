rs.initiate()
rs.add("rs0-1:27017", false)
rs.add("rs0-2:27017", false)
rs.conf()
rs.status()
