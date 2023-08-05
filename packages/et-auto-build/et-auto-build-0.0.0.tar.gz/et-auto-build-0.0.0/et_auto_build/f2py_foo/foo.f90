!-------------------------------------------------------------------------------------------------
! Fortran source code for module et_auto_build.foo
!-------------------------------------------------------------------------------------------------
! Remarks:
!   . Enter Python documentation for this module in ``./foo.rst``.
!     You might want to check the f2py output for the interfaces of the C-wrapper functions.
!     It will be autmatically included in the et_auto_build documentation.
!   . Documument the Fortran routines in this file. This documentation will not be included
!     in the et_auto_build documentation (because there is no recent sphin
!     extension for modern fortran.

subroutine add(x,y,z,n)
  ! Compute the
  !
  ! Python use:
  !    import et-auto-build.foo as f90
  !    a      = np.array([1,2,3],dtype=np.float64)
  !    result = np.ndarray((2,), np.float64)
  !    f90.mean_and_stddev(result,a)
  !    avg = result[0]
  !    std = result[1]
    implicit none
  !-------------------------------------------------------------------------------------------------
    integer*4              , intent(in)    :: n
    real*8   , dimension(n), intent(in)    :: x,y
    real*8   , dimension(n), intent(inout) :: z
    ! intent is inout because we do not want to return an array to avoid needless copying
  !-------------------------------------------------------------------------------------------------
  ! declare local variables
    integer*4 :: i
  !-------------------------------------------------------------------------------------------------
    do i=1,n
        z(i) = x(i) + y(i)
    end do
end subroutine add
