	.file	"restaurant_demo.c"
	.section .rdata,"dr"
	.align 4
LC0:
	.ascii "What you wish to have Veg:1, NonVeg:2. You choice please\0"
LC1:
	.ascii "%d\0"
	.align 4
LC2:
	.ascii "1:DB-Dosa 2:ChowChowBath 3:Idly-Vada 4:BB-Bath. Your choice please: \0"
	.align 4
LC3:
	.ascii "Yummy Davanagere Benne Dosa Maam\0"
	.align 4
LC4:
	.ascii "Spicy kahara bath and tasty Shira\0"
LC5:
	.ascii "Soft Idli and hot Vada Maam\0"
	.align 4
LC6:
	.ascii "Fresh Hot bath with Pure Ghee Sir\0"
	.align 4
LC7:
	.ascii "Sorry we dont serve your choice of food\0"
	.align 4
LC8:
	.ascii "1:Fish-Fry 2:Chicken-Biryani 3:Hanumantu-Palav 4:Egg-Masala. Your choice please: \0"
	.align 4
LC9:
	.ascii "Tasty fish from Mangalore Maam\0"
	.align 4
LC10:
	.ascii "Nati Dum Biryani for you Sir!!!\0"
LC11:
	.ascii "Famous palav for you Maam\0"
LC12:
	.ascii "Delicious Egg masala Maam!!!\0"
	.align 4
LC13:
	.ascii "Sorry we dont serve Lizards and Cockroaches!\0"
	.align 4
LC14:
	.ascii "This is Restaurtant, not Garden. Please Order an item\0"
	.align 4
LC15:
	.ascii "Do you wish to have more? Yes:1, No:Any number\0"
	.text
	.globl	_runMenu
	.def	_runMenu;	.scl	2;	.type	32;	.endef
_runMenu:
LFB10:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	subl	$40, %esp
	movl	$0, -12(%ebp)
	movl	$0, -16(%ebp)
L20:
	movl	$LC0, (%esp)
	call	_puts
	leal	-12(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$LC1, (%esp)
	call	_scanf
	movl	-12(%ebp), %eax
	cmpl	$1, %eax
	je	L3
	cmpl	$2, %eax
	je	L4
	jmp	L21
L3:
	movl	$LC2, (%esp)
	call	_puts
	leal	-16(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$LC1, (%esp)
	call	_scanf
	movl	-16(%ebp), %eax
	cmpl	$2, %eax
	je	L6
	cmpl	$2, %eax
	jg	L7
	cmpl	$1, %eax
	je	L8
	jmp	L5
L7:
	cmpl	$3, %eax
	je	L9
	cmpl	$4, %eax
	je	L10
	jmp	L5
L8:
	movl	$LC3, (%esp)
	call	_puts
	jmp	L11
L6:
	movl	$LC4, (%esp)
	call	_puts
	jmp	L11
L9:
	movl	$LC5, (%esp)
	call	_puts
	jmp	L11
L10:
	movl	$LC6, (%esp)
	call	_puts
	jmp	L11
L5:
	movl	$LC7, (%esp)
	call	_puts
	jmp	L12
L11:
	jmp	L12
L4:
	movl	$LC8, (%esp)
	call	_puts
	leal	-16(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$LC1, (%esp)
	call	_scanf
	movl	-16(%ebp), %eax
	cmpl	$2, %eax
	je	L14
	cmpl	$2, %eax
	jg	L15
	cmpl	$1, %eax
	je	L16
	jmp	L13
L15:
	cmpl	$3, %eax
	je	L17
	cmpl	$4, %eax
	je	L18
	jmp	L13
L16:
	movl	$LC9, (%esp)
	call	_puts
	jmp	L19
L14:
	movl	$LC10, (%esp)
	call	_puts
	jmp	L19
L17:
	movl	$LC11, (%esp)
	call	_puts
	jmp	L19
L18:
	movl	$LC12, (%esp)
	call	_puts
	jmp	L19
L13:
	movl	$LC13, (%esp)
	call	_puts
	jmp	L12
L19:
	jmp	L12
L21:
	movl	$LC14, (%esp)
	call	_puts
L12:
	movl	$LC15, (%esp)
	call	_puts
	leal	-16(%ebp), %eax
	movl	%eax, 4(%esp)
	movl	$LC1, (%esp)
	call	_scanf
	movl	-16(%ebp), %eax
	cmpl	$1, %eax
	je	L20
	nop
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE10:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
	.align 4
LC16:
	.ascii "Welcome to our restaurant The Taste\0"
LC17:
	.ascii "Namaste Visit Again\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB11:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$16, %esp
	call	___main
	movl	$LC16, (%esp)
	call	_puts
	call	_runMenu
	movl	$LC17, (%esp)
	call	_puts
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE11:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	_puts;	.scl	2;	.type	32;	.endef
	.def	_scanf;	.scl	2;	.type	32;	.endef
