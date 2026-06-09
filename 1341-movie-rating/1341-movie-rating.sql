(select u.name as results from Users u join MovieRating m on u.user_id=m.user_id group by u.user_id, u.name order by count(*) desc, u.name limit 1)

union all

(select v.title as results from Movies v join MovieRating z on v.movie_id=z.movie_id where date_format(created_at,'%Y-%m')='2020-02' group by v.movie_id order by avg(rating) desc, v.title limit 1)