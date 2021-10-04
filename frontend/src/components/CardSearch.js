import { Input } from 'antd'

const { Search } = Input

const CardSearch = () => {
    return (
        <div>
            <Search
                placeholder="Search for a card"
                onSearch={value => console.log(value)}
                style={{ width: 200 }}
            />
        </div>
    )
}

export default CardSearch