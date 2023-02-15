db.createUser({
    user: "naia",
    pwd: "password",
    customData: {startDate: new Date()},
    roles: [
        {role: "clusterAdmin", db: "admin"},
        {role: "readAnyDatabase", db: "admin"},
        "readWrite"
    ]
})