// Inheritance ---> one 

// class A ---> class B

// Simple / Single Inheritance

// class A{// Parent Class
//     a(){
//         console.log("A Property ")
//     }
// }

// class B extends A{// Child Class
//     b(){
//         console.log("B Property")
//     }
// }

// const obj = new B()

// obj.a()

// Multilevel Inheritance --->. 

// g ---> p  --> c

// class A{// Grand Parent 
//     a(){
//         console.log("Grand Parent Property")
//     }
// }
// class B extends A{// Parent
//     b(){
//         console.log("Parent Class Property")
//     }
// }
// class C extends B {// Child
//     c(){
//         console.log("Child Class Property")
//     }
// }
// const obj = new C()

// obj.a()
// obj.b()
// obj.c()


// Hierarchical Inheritance ---> 

//     p 
//.   /  \
//.  c    c 



// class A{// Parent 
//     a(){
//         console.log("Grand Parent Property")
//     }
// }
// class B extends A{// Child 1
//     b(){
//         console.log("Parent Class Property")
//     }
// }
// class C extends A {// Child 2
//     c(){
//         console.log("Child Class Property")
//     }
// }
// const obj = new C()

// obj.a()
// // obj.b()
// obj.c()

