! Lab 4, task 1

program task1
    implicit none
    integer :: i1
    integer, parameter :: N=5, display_iteration = 0
    real(kind=8) :: odd_sum

    odd_sum = 0.d0
    
    do i1 = 1, N, 2
        odd_sum = odd_sum + i1
    end do

    print *, 'Sum = ', odd_sum
end program task1

! To compile this code:
! $ gfortran -o task1.exe lab41.f90
! To run the resulting executable: $ ./task1.exe
