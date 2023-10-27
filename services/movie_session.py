from datetime import datetime, timedelta
from db.models import MovieSession
from typing import List, Optional


def create_movie_session(
        movie_show_time: datetime,
        movie_id: int,
        cinema_hall_id: int) -> MovieSession:
    return MovieSession.objects.create(
        show_time=movie_show_time,
        movie_id=movie_id,
        cinema_hall_id=cinema_hall_id
    )


def get_movies_sessions(
        session_date: Optional[str] = None) -> List[MovieSession]:
    queryset = MovieSession.objects.all()

    if session_date:
        start_date = datetime.strptime(
            session_date,
            "%Y-%m-%d")
        end_date = start_date + timedelta(days=1)
        queryset = queryset.filter(
            show_time__gte=start_date,
            show_time__lt=end_date)

    return queryset


def get_movie_session_by_id(session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=session_id)


def update_movie_session(
        session_id: int,
        show_time: Optional[datetime] = None,
        movie_id: Optional[int] = None,
        cinema_hall_id: Optional[int] = None) -> MovieSession:
    movie_session = MovieSession.objects.get(id=session_id)

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie_session.movie_id = movie_id

    if cinema_hall_id:
        movie_session.cinema_hall_id = cinema_hall_id

    movie_session.save()
    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = MovieSession.objects.get(id=session_id)
    movie_session.delete()