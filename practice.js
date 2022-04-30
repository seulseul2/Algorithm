const firstName = 'Brandan'
const lastName = 'Eich'
const fullName = `${firstName} ${lastName}`

const noArgs = function () {
    return 0
}

const twoArgs = function (arg1, arg2) {
    return [arg1, arg2]
}

const threeArgs = function(arg1, arg2, arg3) {
    return [arg1, arg2, arg3]
}

threeArgs()
threeArgs(1)
threeArgs(1, 2)

const restOpr = function (arg1, arg2, ...restArgs) {
    return [arg1, arg2, restArgs]
}

restOpr(1, 2, 3, 4, 5)
restOpr(1, 2)


const spreadOpr = function (arg1, arg2, arg3) {
    return arg1 + arg2 + arg3
}

const numbers = [1, 2, 3]
spreadOpr(...numbers)


const arrow1 = function (name) {
    return `hello, ${name}`
}

const arrow2 = name =>
    `hello, ${name}`
