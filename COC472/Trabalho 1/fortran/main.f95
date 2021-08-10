program main
    implicit none

    ! Constants declaration
    integer :: ARR_SIZE, JI_LOOP, i, j
    real(8) :: start, end, number
    real(8), dimension(:,:), allocatable :: A
    real(8), dimension (:), allocatable :: x
    real(8), dimension (:), allocatable :: b
    character(len=32) :: arg

    ! Checks for 'ARR_SIZE' and 'JI_LOOP' values in argv
    call getarg(1, arg)
    read(arg, "(I10)") ARR_SIZE
    
    call getarg(2, arg)
    read(arg, "(I1)") JI_LOOP

    ! Allocates memory for the matrixes
    allocate(A(ARR_SIZE, ARR_SIZE))
    allocate(x(ARR_SIZE))
    allocate(b(ARR_SIZE))

    call random_seed()

    do i = 1, ARR_SIZE
        call random_number(number)
        x(i) = number * (ARR_SIZE + 1)
        b(i) = 0
        do j = 1, ARR_SIZE
            call random_number(number)
            A(i, j) = number * (ARR_SIZE + 1)
        end do
    end do

    call cpu_time(start)
    if (JI_LOOP == 1) then
        do i = 1, ARR_SIZE
            do j = 1, ARR_SIZE
                b(i) = A(j, i) * x(j)
            end do
        end do
    else
        do i = 1, ARR_SIZE
            do j = 1, ARR_SIZE
                b(i) = A(i, j) * x(j)
            end do
        end do
    end if
    call cpu_time(end)

    print *, (end - start)

    contains

    subroutine get_random()
        implicit none
        
        integer :: ARR_SIZE, i
        integer :: RAND_SIZE = 100
        real(8) :: number

        do i = 1, ARR_SIZE
            call random_number(number)
            x(i) = number * RAND_SIZE
        end do 
    end

end program main